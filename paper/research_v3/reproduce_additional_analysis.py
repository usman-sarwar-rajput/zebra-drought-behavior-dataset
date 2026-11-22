from pathlib import Path
import sys,os,ast,json,shutil,hashlib
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
import numpy as np,pandas as pd,patsy
from scipy import stats,linalg
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
# Reuse the previously audited fitting function without executing the seven-species workflow.
tree=ast.parse((ROOT/'scripts/reproduce.py').read_text())
func=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='regression')
exec(compile(ast.Module(body=[func],type_ignores=[]),'regression','exec'))
manifest=[]
for slug in ['zebra']:
    src=ROOT/'analysis';dest=ROOT
    dest.mkdir(exist_ok=True);out=dest/'analysis';out.mkdir(exist_ok=True)
    d=pd.read_csv(src/'analysis_data.csv',dtype={'unit':str})
    assert d.outcome.gt(0).all() and not d.duplicated(['unit','date']).any()
    monthly=slug=='elephant'
    formula='dryness+C(unit)+C(month)+C(year)' if monthly else 'C(unit)+C(phase)'
    if not monthly:d['phase']=pd.Categorical(d.phase,categories=['CD','HD','HW'])
    terms={'one_unit_drier':{'dryness':1}} if monthly else {'HD_vs_CD':{'C(phase)[T.HD]':1},'HW_vs_CD':{'C(phase)[T.HW]':1},'HW_vs_HD':{'C(phase)[T.HW]':1,'C(phase)[T.HD]':-1}}
    r=pd.DataFrame(regression(d,formula,'refit_primary',terms,slug,'monthly' if monthly else 'daily'))
    old=pd.read_csv(src/'statistical_results.csv').query("model=='primary'").set_index('contrast')
    for v in r.itertuples():
        for k in ['change_pct','low_pct','high_pct','p']:
            assert np.isclose(getattr(v,k),old.loc[v.contrast,k],rtol=1e-7)
    r.to_csv(out/'primary_refit_check.csv',index=False)
    loo=[]
    for unit in d.unit.unique():
        rr=regression(d[d.unit!=unit],formula,'leave_one_animal_out',terms,slug,'monthly' if monthly else 'daily')
        for row in rr:row['excluded_animal']=unit
        loo.extend(rr)
    loo=pd.DataFrame(loo);loo.to_csv(out/'leave_one_animal_out.csv',index=False)
    lo=loo.groupby('contrast').agg(min_change_pct=('change_pct','min'),max_change_pct=('change_pct','max'),positive_fits=('change_pct',lambda s:int((s>0).sum())),fits=('change_pct','size')).reset_index()
    lo.to_csv(out/'leave_one_animal_out_summary.csv',index=False)
    fig,ax=plt.subplots(figsize=(8.4,3.3),layout='constrained')
    for j,(contrast,g) in enumerate(loo.groupby('contrast')):
        ax.scatter(g.change_pct,np.repeat(j,len(g)),s=25,color='#287d8e',alpha=.7)
        ax.scatter([old.loc[contrast,'change_pct']],[j],marker='D',s=60,color='black')
    ax.set_yticks(range(len(lo)),lo.contrast.str.replace('_',' '));ax.axvline(0,ls='--',color='gray');ax.set_xlabel('Estimated change (%) after omitting one animal');ax.set_title('Individual sensitivity of the statistical estimate\nBlack diamond is the full-sample estimate')
    fig.savefig(dest/'figures/09_individual_sensitivity.png',dpi=220);plt.close(fig)
    if not monthly:
        means=d.groupby(['unit','phase'],observed=True).outcome.mean().unstack().reindex(columns=['CD','HD','HW'])
        means.to_csv(out/'animal_period_arithmetic_means.csv')
        desc=[]
        for ph in ['CD','HD','HW']:
            z=d[d.phase==ph];desc.append(dict(phase=ph,animal_days=len(z),animals=z.unit.nunique(),first=z.date.min(),last=z.date.max(),pooled_mean=z.outcome.mean(),equal_animal_mean=means[ph].mean(),pooled_median=z.outcome.median()))
        pd.DataFrame(desc).to_csv(out/'observed_period_summary.csv',index=False)
        paired=[]
        for a,b in [('CD','HD'),('CD','HW'),('HD','HW')]:
            u=means[[a,b]].dropna();delta=u[b]-u[a]
            paired.append(dict(contrast=b+'_vs_'+a,paired_animals=len(u),earlier_mean=u[a].mean(),later_mean=u[b].mean(),arithmetic_change_pct=100*(u[b].mean()/u[a].mean()-1),animals_increased=int((delta>0).sum()),animals_decreased=int((delta<0).sum())))
        pd.DataFrame(paired).to_csv(out/'paired_period_descriptives.csv',index=False)
        fig,ax=plt.subplots(figsize=(8.4,3.5),layout='constrained')
        for unit,row in means.iterrows():ax.plot(range(3),row,marker='o',lw=1,alpha=.75,label=unit)
        ax.set_xticks(range(3),['Cool drought','Hot drought','Rainy recovery']);ax.set_ylabel('Mean daily movement (km/day)');ax.legend(fontsize=7,ncol=3);ax.set_title('Observed individual period means\nMissing periods are not interpolated')
        fig.savefig(dest/'figures/08_observed_periods.png',dpi=220);plt.close(fig)
    else:
        ar=out
        rr=pd.read_csv(ar/'calendar_complete_stage_records.csv',dtype={'unit':str})
        order=['Earlier comparison','Near before','During drought','Early after','Later comparison']
        rr['stage']=pd.Categorical(rr.stage,categories=order,ordered=True)
        events=pd.read_csv(ar/'calendar_event_audit.csv');events=events[events.complete]
        events['onset_year']=pd.to_datetime(events.onset).dt.year
        rr=rr.merge(events[['event','onset_year']],on='event',validate='many_to_one')
        diag=[]
        for name,g in [('all_calendar_sequences',rr)]+[(f'exclude_onset_year_{year}',rr[rr.onset_year!=year]) for year in sorted(rr.onset_year.unique())]:
            X=patsy.dmatrix('C(unit)+C(stage)+C(month)',g,return_type='dataframe');x=np.asarray(X);pinv=np.linalg.pinv(x);bad=[]
            for col in X.columns:
                if col.startswith('C(stage)'):
                    c=np.zeros(x.shape[1]);c[X.columns.get_loc(col)]=1
                    if np.linalg.norm(c-c@pinv@x)>1e-7:bad.append(col)
            diag.append(dict(sample=name,animals=g.unit.nunique(),events=g.event.nunique(),rows=len(g),rank=int(np.linalg.matrix_rank(x)),columns=x.shape[1],nonidentifiable_contrasts=bad))
        (out/'calendar_stage_identification.json').write_text(json.dumps(diag,indent=2))
    # Recalculate all reported prediction errors from saved out-of-sample predictions.
    pred=pd.read_csv(out/'out_of_sample_predictions.csv');scores=pd.read_csv(out/'ai_scores.csv')
    for row in scores.itertuples():
        q=pred[(pred.design==row.design)&(pred.model==row.model)]
        assert np.isclose(np.abs(q.predicted_log-np.log(q.observed)).mean(),row.log_MAE)
    manifest.append(dict(species=slug,records=len(d),animals=d.unit.nunique(),primary_refit='matched',leave_one_animal_out_fits=d.unit.nunique(),prediction_errors='recomputed and matched',input_sha256=hashlib.sha256((src/'analysis_data.csv').read_bytes()).hexdigest()))
    print(slug,lo.to_dict('records'),flush=True)
(ROOT/'analysis_validation.json').write_text(json.dumps(manifest,indent=2))
