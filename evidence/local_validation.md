# Local validation evidence

Ngày kiểm tra: 2026-08-21

## Tests

```text
python -m pytest tests/ -v
======================= 3 passed, 23 warnings in 13.60s =======================
```

## MLflow runs

```text
Accuracy: 0.5640 | F1: 0.5534
Accuracy: 0.5580 | F1: 0.5185
Accuracy: 0.6440 | F1: 0.6417
Accuracy: 0.6800 | F1: 0.6786
```

## Continuous-training simulation

```text
Cap nhat du lieu: 2998 -> 5996 mau
Accuracy: 0.7500 | F1: 0.7486
```

## FastAPI smoke test

```text
GET /health
{"status":"ok"}

POST /predict (12 features)
{"prediction":0,"label":"thap"}
```

## Workflow syntax

```text
python evidence\check_workflow_yaml.py
Workflow YAML parsed; four jobs found.
```

## DVC transition check

```text
Bước 3: dvc add data/train_phase1.csv sau khi 2998 -> 5996 mẫu
pointer mới: md5=5853e7711c78f02286e65fca6cb6e124, size=368068
Khôi phục dataset phase 1 và dvc add lại
pointer cuối: md5=c43afab731fd6431a94f888fdc687876, size=184090
dvc status: Data and pipelines are up to date.
```
