# Test Record Template

Copy to `tests/logs/<TEST_ID>_YYYYMMDD.md` for each session.

```yaml
test_id: T-0X
date: YYYY-MM-DD
operators: []
lso_authorization: PENDING | signed name
configuration:
  laser_sku: 
  doe_sku:
  collimator:
  max_power_authorized_w:
  mode: ALIGN | PULSE
environment:
  lab:
  ambient_c:
results_summary:
pass_fail: PASS | FAIL | INCONCLUSIVE
data_files: []
deviations:
notes:
lso_review:
```

Raw CSV columns for T-02:

```
range_m, beamlet_id, power_w, irradiance_w_m2, meter_serial, notes
```

Raw CSV columns for T-04:

```
time_s, current_a, voltage_v, power_w, temp_c, mode, notes
```
