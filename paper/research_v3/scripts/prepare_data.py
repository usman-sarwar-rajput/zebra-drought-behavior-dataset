from pathlib import Path
import json
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def prepare():
 m=json.loads((ROOT/'analysis/study_metadata.json').read_text());s=m['slug']
 p=pd.read_csv(ROOT/'source/source_records.csv',dtype={'ID':str})
 if s=='elephant':
  d=pd.DataFrame({'unit':p.ID,'animal':p.ID,'date':p.date,'outcome':p.monthlyHomeRange_km2,'index':p.SPEI03,'annual_index':p.SPEI12})
 elif m['kind']=='monthly':
  assert p.groupby(['social_group','YearMon']).threemonth_spi.nunique().max()==1
  d=p.groupby(['social_group','YearMon']).agg(outcome=('hr_area','mean'),index=('threemonth_spi','first'),annual_index=('prevyear_spi','first'),animal=('id_simple',lambda x:';'.join(sorted(x.unique())))).reset_index().rename(columns={'social_group':'unit','YearMon':'date'})
 else:
  d=p.rename(columns={'id':'unit','day':'date','V1':'outcome','season':'phase'});d['animal']=d.unit
 d.unit=d.unit.astype(str);d['date']=pd.to_datetime(d.date,format='mixed');d=d.sort_values(['date','unit']).reset_index(drop=True)
 d['month']=d.date.dt.month;d['year']=d.date.dt.year;d['monthnum']=d.year*12+d.month
 d['sin_month']=np.sin(2*np.pi*d.month/12);d['cos_month']=np.cos(2*np.pi*d.month/12)
 if m['kind']=='monthly':d['dryness']=-d['index'];d['annual_dryness']=-d.annual_index
 return d
if __name__=='__main__':
 out=ROOT/'reproduced';out.mkdir(exist_ok=True);prepare().to_csv(out/'prepared_data.csv',index=False)
 print('Prepared',len(prepare()),'records')
