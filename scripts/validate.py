from pathlib import Path
import hashlib,json
import numpy as np
import pandas as pd
from prepare_data import prepare
ROOT=Path(__file__).resolve().parents[1]
for path,digest in json.loads((ROOT/'CHECKSUMS.json').read_text()).items():
 assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
m=json.loads((ROOT/'analysis/study_metadata.json').read_text())
d=pd.read_csv(ROOT/'data/analysis_data.csv',dtype={'unit':str,'animal':str},parse_dates=['date'])
pd.testing.assert_frame_equal(prepare(),d,check_dtype=False,rtol=1e-10,atol=1e-10)
assert len(d)==m['rows'] and d.unit.nunique()==m['units_count']
assert not d.duplicated(['unit','date']).any() and d.outcome.gt(0).all()
p=pd.read_csv(ROOT/'analysis/out_of_sample_predictions.csv',dtype={'unit':str})
a=pd.read_csv(ROOT/'analysis/ai_scores.csv')
for row in a.itertuples():
 g=p[(p.design==row.design)&(p.model==row.model)];e=g.predicted_log-np.log(g.observed)
 assert np.isclose(np.abs(e).mean(),row.log_MAE)
 assert np.isclose(np.sqrt(np.mean(e*e)),row.log_RMSE)
 assert np.isclose(g.assign(error=np.abs(e)).groupby('unit').error.mean().mean(),row.equal_unit_log_MAE)
 assert np.isclose(np.abs(g.predicted-g.observed).mean(),row.raw_MAE)
for row in pd.read_csv(ROOT/'analysis/validation_splits.csv').itertuples():
 if row.design=='held_out_units':assert row.shared_units==0
 else:assert pd.Timestamp(row.last_train)<pd.Timestamp(row.first_test)-pd.Timedelta(days=31 if m['kind']=='monthly' else 7)
rebuilt=ROOT/'reproduced'/m['slug']
if rebuilt.exists():
 for name in ['analysis_data.csv','statistical_results.csv','ai_scores.csv','out_of_sample_predictions.csv','validation_splits.csv']:
  original=ROOT/('data' if name=='analysis_data.csv' else 'analysis')/name
  expected=pd.read_csv(original);actual=pd.read_csv(rebuilt/name)
  pd.testing.assert_frame_equal(expected,actual,check_dtype=False,rtol=1e-7,atol=1e-8)
print(json.dumps({'species':m['slug'],'records':len(d),'units':d.unit.nunique(),'checksums':'passed','source_preprocessing':'passed','saved_prediction_metrics':'passed','split_audit':'passed','reproduction':'passed' if rebuilt.exists() else 'not run'}))
