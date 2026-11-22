"""Single-species adaptation of the original saved analysis; outputs go to reproduced/."""
from pathlib import Path
import os,sys,json,hashlib
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import numpy as np
import pandas as pd
from scipy import stats,linalg
import patsy,joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GroupKFold
from statsmodels.stats.multitest import multipletests
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'reproduced';OUT.mkdir(exist_ok=True)
STAGES=['Baseline','Near-before','During','Early-after','Late-normal']
SEED=20261122
from prepare_data import prepare
meta=json.loads((ROOT/'analysis/study_metadata.json').read_text())
studies={meta['slug']:(prepare(),meta)}
def stage_audit(d,kind):
 if kind=='daily':
  return pd.DataFrame(),{'candidate_events':0,'complete_events':0,'complete_units':0,'stages':{s:0 for s in STAGES},'reason':'No independent onset, baseline or late-normal labels. CD/HD/HW are not the requested five stages.'}
 records=[];events=[];eid=0
 for unit,g in d.groupby('unit'):
  g=g.sort_values('monthnum').set_index('monthnum');runs=[];run=[]
  for n in g.index:
   if g.loc[n,'index']<=-1:
    if run and n!=run[-1]+1:runs.append(run);run=[]
    run.append(n)
   elif run:runs.append(run);run=[]
  if run:runs.append(run)
  for run in runs:
   near=[run[0]-2,run[0]-1]
   if len(run)<2 or not all(n in g.index for n in near) or not g.loc[near,'index'].gt(-1).all():continue
   eid+=1
   windows={'Baseline':[run[0]-4,run[0]-3],'Near-before':near,'During':run,'Early-after':[run[-1]+1,run[-1]+2],'Late-normal':[run[-1]+3,run[-1]+4]}
   good={}
   for stage,nn in windows.items():
    valid=all(n in g.index for n in nn)
    if valid and stage=='Late-normal':valid=bool(g.loc[nn,'index'].ge(0).all())
    elif valid and stage!='During':valid=bool(g.loc[nn,'index'].gt(-1).all())
    good[stage]=valid
   # Late normal must follow a validated early exit, not a new intervening drought.
   good['Late-normal']=good['Late-normal'] and good['Early-after']
   complete=all(good.values());events.append({'event':eid,'unit':unit,'complete':complete,**good})
   for stage,nn in windows.items():
    if good[stage]:
     for n in nn:records.append(dict(g.loc[n].to_dict(),stage=stage,event=eid,complete=complete,monthnum=n))
 e=pd.DataFrame(events);long=pd.DataFrame(records)
 result={'candidate_events':len(e),'complete_events':int(e.complete.sum()) if len(e) else 0,'complete_units':int(e.loc[e.complete,'unit'].nunique()) if len(e) else 0,'stages':{s:int(e[s].sum()) if len(e) else 0 for s in STAGES},'reason':'Counts are available event-stage windows, not independent disasters. Late-normal is environmental only.'}
 return long,result

allstat=[];allai=[];summaries=[]
def regression(data,formula,name,terms,slug,kind):
 X=patsy.dmatrix(formula,data,return_type='dataframe');rank=np.linalg.matrix_rank(X)
 if rank<X.shape[1]:
  _,_,pv=linalg.qr(np.asarray(X),mode='economic',pivoting=True);keep=sorted(pv[:rank]);removed=set(X.columns)-set(X.columns[keep])
  if any(t in removed for contrast in terms.values() for t in contrast):return [{'species':slug,'model':name,'status':'not_identifiable'}]
  X=X.iloc[:,keep]
 x=np.asarray(X);pinv=np.linalg.pinv(x);y=np.log(data.outcome.to_numpy());b=pinv@y;r=y-x@b;n=len(y);rank=x.shape[1]
 assert np.allclose(b,np.linalg.lstsq(x,y,rcond=None)[0],atol=1e-8)
 gs=[pd.factorize(data.unit)[0]]
 if kind=='monthly':gs+=[pd.factorize(data.year)[0],pd.factorize(pd.MultiIndex.from_arrays([data.unit,data.year]))[0]]
 cnt=[len(np.unique(z)) for z in gs];df=(min(cnt[:2]) if kind=='monthly' else cnt[0])-1
 rows=[]
 for term,weights in terms.items():
  c=np.zeros(rank)
  for key,val in weights.items():c[X.columns.get_loc(key)]=val
  score=(c@pinv)*r;vv=[]
  for gg,G in zip(gs,cnt):
   sums=np.zeros(G);np.add.at(sums,gg,score);vv.append(float((sums*sums).sum()*G/(G-1)*(n-1)/(n-rank)))
  v=max(vv[0],vv[1],vv[0]+vv[1]-vv[2]) if kind=='monthly' else vv[0]
  se=np.sqrt(v);coef=float(c@b);t=stats.t.ppf(.975,df);p=float(2*stats.t.sf(abs(coef/se),df))
  rows.append(dict(species=slug,model=name,contrast=term,status='estimated',n=n,units=cnt[0],time_clusters=cnt[1] if kind=='monthly' else None,df=df,change_pct=100*np.expm1(coef),low_pct=100*np.expm1(coef-t*se),high_pct=100*np.expm1(coef+t*se),p=p,log_coefficient=coef))
 return rows

for slug,(d,meta) in studies.items():
 folder=OUT/slug;folder.mkdir(exist_ok=True);d=d.copy();d.unit=d.unit.astype(str);d['date']=pd.to_datetime(d.date,format='mixed');d=d.sort_values(['date','unit']).reset_index(drop=True)
 d['month']=d.date.dt.month;d['year']=d.date.dt.year;d['monthnum']=d.year*12+d.month
 d['sin_month']=np.sin(2*np.pi*d.month/12);d['cos_month']=np.cos(2*np.pi*d.month/12)
 assert not d.duplicated(['unit','date']).any() and (d.outcome>0).all()
 if meta['kind']=='monthly':d['dryness']=-d['index'];d['annual_dryness']=-d.annual_index
 else:d['phase']=pd.Categorical(d.phase,categories=['CD','HD','HW'])
 d.to_csv(folder/'analysis_data.csv',index=False)
 long,stage=stage_audit(d,meta['kind']);long.to_csv(folder/'stage_records.csv',index=False)
 meta.update(rows=len(d),units_count=d.unit.nunique(),first=str(d.date.min().date()),last=str(d.date.max().date()),stages=stage,slug=slug)
 if meta['kind']=='monthly':meta.update(drought_rows=int((d['index']<=-1).sum()),index_min=float(d['index'].min()),index_max=float(d['index'].max()),annual_drought_rows=int((d.annual_index<=-1).sum()))
 if meta['kind']=='monthly':
  st=[]
  for name,exp,nuisance in [('primary','dryness','C(unit)+C(month)+C(year)'),('season_only_sensitivity','dryness','C(unit)+C(month)'),('annual_sensitivity','annual_dryness','C(unit)+C(month)+C(year)')]:
   st+=regression(d,exp+'+'+nuisance,name,{'one_unit_drier':{exp:1}},slug,'monthly')
 else:
  terms={'HD_vs_CD':{'C(phase)[T.HD]':1},'HW_vs_CD':{'C(phase)[T.HW]':1},'HW_vs_HD':{'C(phase)[T.HW]':1,'C(phase)[T.HD]':-1}}
  st=regression(d,'C(unit)+C(phase)','primary',terms,slug,'daily')
  if slug=='wildebeest':st+=regression(d[d.unit!='3317CT33'],'C(unit)+C(phase)','omit_low_movement_individual',terms,slug,'daily')
 allstat+=st
 # Features contain contemporaneous climate, never future outcomes or identifiers.
 seasonal=['sin_month','cos_month'];features=seasonal+(['dryness'] if meta['kind']=='monthly' else [])
 models=['mean','seasonal_ridge','seasonal_forest']+(['climate_forest'] if meta['kind']=='monthly' else [])
 splits=[]
 for fold,(tr,te) in enumerate(GroupKFold(n_splits=min(5,d.unit.nunique())).split(d,groups=d.unit)):
  assert not set(d.iloc[tr].unit)&set(d.iloc[te].unit)
  splits.append(('held_out_units',fold,tr,te))
 dates=np.sort(d.date.unique());blocks=np.array_split(dates,4) if meta['kind']=='monthly' else [np.array(g.date.unique()) for _,g in d.groupby('monthnum')]
 for fold,block in enumerate(blocks[1:]):
  start=pd.Timestamp(block.min());embargo=pd.Timedelta(days=31 if meta['kind']=='monthly' else 7)
  tr=np.flatnonzero((d.date<start-embargo).to_numpy());te=np.flatnonzero(d.date.isin(block).to_numpy())
  if len(tr)<8 or len(te)<2:continue
  assert d.iloc[tr].date.max()<d.iloc[te].date.min()-embargo
  splits.append(('forward_time',fold,tr,te))
 preds=[];splitlog=[]
 for design,fold,tr,te in splits:
  train=d.iloc[tr];test=d.iloc[te];y=np.log(train.outcome)
  splitlog.append(dict(design=design,fold=fold,train_rows=len(tr),test_rows=len(te),train_units=train.unit.nunique(),test_units=test.unit.nunique(),last_train=str(train.date.max()),first_test=str(test.date.min()),shared_units=len(set(train.unit)&set(test.unit))))
  for model in models:
   cols=features if model=='climate_forest' else seasonal
   if model=='mean':yp=np.repeat(y.mean(),len(te))
   else:
    estimator=make_pipeline(StandardScaler(),Ridge(alpha=1.0)) if model=='seasonal_ridge' else RandomForestRegressor(n_estimators=120,max_depth=5,min_samples_leaf=max(3,int(len(tr)*.03)),random_state=SEED,n_jobs=1)
    estimator.fit(train[cols],y);yp=estimator.predict(test[cols])
   for i,pred in zip(te,yp):preds.append(dict(design=design,fold=fold,model=model,row=int(i),unit=d.loc[i,'unit'],date=str(d.loc[i,'date'].date()),observed=float(d.loc[i,'outcome']),predicted_log=float(pred),predicted=float(np.exp(pred))))
 pred=pd.DataFrame(preds);pred.to_csv(folder/'out_of_sample_predictions.csv',index=False);pd.DataFrame(splitlog).to_csv(folder/'validation_splits.csv',index=False)
 scores=[]
 for (design,model),g in pred.groupby(['design','model']):
  e=g.predicted_log-np.log(g.observed);u=g.assign(ae=np.abs(e)).groupby('unit').ae.mean()
  scores.append(dict(species=slug,design=design,model=model,test_rows=len(g),test_units=g.unit.nunique(),log_MAE=float(np.abs(e).mean()),equal_unit_log_MAE=float(u.mean()),log_RMSE=float(np.sqrt(np.mean(e*e))),raw_MAE=float(np.abs(g.predicted-g.observed).mean())))
 allai+=scores
 final=RandomForestRegressor(n_estimators=120,max_depth=5,min_samples_leaf=max(3,int(len(d)*.03)),random_state=SEED,n_jobs=1).fit(d[features],np.log(d.outcome))
 joblib.dump(final,folder/'exploratory_random_forest.joblib');(folder/'model_features.json').write_text(json.dumps({'features':features,'target':'natural logarithm of '+meta['outcome'],'seed':SEED,'warning':'Contemporaneous prediction, not an early-warning or five-stage classifier. Full-data model; performance must come from held-out predictions.'},indent=2))
 # Four scientific panels, saved separately for readable manuscript pages.
 fig,ax=plt.subplots(figsize=(8.2,3.0));counts=[stage['stages'][s] for s in STAGES]
 ax.bar(STAGES,counts,color=['#577590','#43aa8b','#f8961e','#f3722c','#8e7dbe']);ax.set_ylim(0,max(counts+[1])*1.35);ax.set_ylabel('Available event-stage windows');ax.set_title(meta['name']+': five-stage coverage')
 for i,n in enumerate(counts):ax.text(i,n+.04*max(counts+[1]),str(n),ha='center')
 ax.text(.99,.94,f"Complete events: {stage['complete_events']}",transform=ax.transAxes,ha='right',va='top')
 if meta['kind']=='daily':ax.text(.5,.45,'CD / HD / HW are observed, but cannot supply five stages',ha='center',transform=ax.transAxes,fontsize=9)
 fig.tight_layout();fig.savefig(folder/'figure_1_stage_coverage.png',dpi=180);plt.close(fig)
 fig,axes=plt.subplots(1,2,figsize=(8.2,3.1))
 for unit,g in d.groupby('unit'):axes[0].plot(g.date,g.outcome,alpha=.4,lw=.7,marker='.',markersize=2)
 axes[0].set_yscale('log');axes[0].set_ylabel(meta['outcome']+' ('+meta['units']+')');axes[0].set_title('Observed records by unit');axes[0].tick_params(axis='x',rotation=30,labelsize=7)
 if meta['kind']=='monthly':axes[1].scatter(d['index'],d.outcome,s=10,alpha=.5);axes[1].axvline(-1,color='firebrick',ls='--',lw=1);axes[1].set_xlabel(meta['index_name'])
 else:
  for j,ph in enumerate(['CD','HD','HW']):
   vals=d[d.phase==ph].groupby('unit').outcome.mean();axes[1].scatter(np.repeat(j,len(vals)),vals,s=22,alpha=.7)
  axes[1].set_xticks([0,1,2],['Cool drought','Hot drought','Rainy recovery'],rotation=15,fontsize=8)
 axes[1].set_yscale('log');axes[1].set_title('Exposure and behavior (unadjusted)');fig.tight_layout();fig.savefig(folder/'figure_2_observations.png',dpi=180);plt.close(fig)
 # AI figures use honest held-out predictions, never fitted training values.
 ai=pd.DataFrame(scores);fig,axes=plt.subplots(1,2,figsize=(8.2,3.1))
 for j,design in enumerate(['held_out_units','forward_time']):
  s=ai[ai.design==design];axes[j].barh(s.model,s.log_MAE,color='#277da8');axes[j].set_xlabel('Held-out log-MAE (lower is better)');axes[j].set_title(design.replace('_',' '));axes[j].tick_params(axis='y',labelsize=8)
 fig.tight_layout();fig.savefig(folder/'figure_4_ai_validation.png',dpi=180);plt.close(fig)
 (folder/'study_metadata.json').write_text(json.dumps(meta,indent=2,default=str),encoding='utf8');summaries.append(meta)
 print(slug,meta['rows'],'rows',meta['units_count'],'units',stage,'AI done',flush=True)

r=pd.DataFrame(allstat);r['q_primary_family']=np.nan
family=pd.read_csv(ROOT/'analysis/multiplicity_family.csv');family=family[(family.model=='primary')&family.p.notna()].copy()
for ix,row in r[r.model=='primary'].iterrows():
 family.loc[(family.species==row.species)&(family.contrast==row.contrast),'p']=row.p
family['q']=multipletests(family.p,method='fdr_bh')[1]
for ix,row in r[r.model=='primary'].iterrows():
 r.loc[ix,'q_primary_family']=family.loc[(family.species==row.species)&(family.contrast==row.contrast),'q'].iloc[0]
r.to_csv(OUT/'all_statistical_results.csv',index=False);pd.DataFrame(allai).to_csv(OUT/'all_ai_scores.csv',index=False)
for meta in summaries:
 slug=meta['slug'];folder=OUT/slug;s=r[(r.species==slug)&(r.status=='estimated')];s.to_csv(folder/'statistical_results.csv',index=False);pd.DataFrame(allai).query('species==@slug').to_csv(folder/'ai_scores.csv',index=False)
 fig,ax=plt.subplots(figsize=(8.2,3.0));pos=np.arange(len(s));ax.errorbar(s.change_pct,pos,xerr=np.vstack([s.change_pct-s.low_pct,s.high_pct-s.change_pct]),fmt='o',color='#277da8',capsize=3);ax.set_yticks(pos,(s.model+': '+s.contrast).str.replace('_',' '),fontsize=8);ax.axvline(0,color='gray',lw=1);ax.set_xlabel('Estimated % change with nominal uncertainty band');ax.set_title(meta['name']+': separate statistical models');fig.tight_layout();fig.savefig(folder/'figure_3_statistics.png',dpi=180);plt.close(fig)

print("Species analysis complete")
