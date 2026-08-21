# Báo cáo Lab MLOps Day 21 — Wine Quality

## 1. Mục tiêu

Xây dựng quy trình MLOps cho bài toán phân loại chất lượng rượu vang: theo dõi thí nghiệm bằng MLflow, quản lý dữ liệu bằng DVC, tự động kiểm thử/huấn luyện/đánh giá/triển khai bằng GitHub Actions và phục vụ model qua FastAPI trên Google Compute Engine.

## 2. Kết quả triển khai

- `src/train.py`: huấn luyện Random Forest, ghi params và metrics (`accuracy`, `f1_score`) vào MLflow, tạo `outputs/metrics.json` và `models/model.pkl`.
- `src/serve.py`: cung cấp `GET /health` và `POST /predict`, kiểm tra đúng 12 features.
- `tests/test_train.py`: 3 unit tests kiểm tra kết quả train, metrics và model artifact.
- DVC quản lý ba dataset; remote được cấu hình tại `gs://vinuni-lab16-phong-2026-mlops/dvc`.
- GitHub Actions gồm bốn jobs: `Unit Test → Train → Eval → Deploy`.
- VM `mlops-serve` chạy FastAPI và lấy model mới nhất từ GCS.

## 3. Thí nghiệm và chất lượng model

Các thí nghiệm local được ghi nhận bằng MLflow. Bộ tham số tốt nhất được lưu trong `params.yaml`:

```yaml
n_estimators: 500
max_depth: null
min_samples_split: 5
```

Với dữ liệu Bước 2 gồm 2998 mẫu, kết quả tốt nhất là:

```text
accuracy = 0.6800
f1_score = 0.6786
```

Do accuracy thấp hơn ngưỡng `0.70`, Eval gate đã chặn Deploy. Đây là hành vi đúng theo thiết kế CI/CD và được minh chứng tại `evidence/04-eval-gate-failed-0.68.png`.

Ở Bước 3, `train_phase2.csv` được bổ sung vào dữ liệu train, nâng số mẫu từ 2998 lên 5996. Kết quả:

```text
accuracy = 0.7500
f1_score = 0.7486
```

Model mới vượt Eval gate và được triển khai thành công.

## 4. Kiểm thử và minh chứng

- `python -m pytest tests/ -q`: **3 passed**.
- Workflow YAML: hợp lệ, đủ 4 jobs.
- `dvc status`: **Data and pipelines are up to date**.
- DVC push thành công lên GCS.
- API VM trả kết quả dự đoán hợp lệ: `prediction=0`, `label=thap`.
- GCS chứa `models/latest/model.pkl`.
- Run B3 được kích hoạt bởi commit dữ liệu `4001541` với event `push`; cả bốn jobs hoàn thành thành công.

Minh chứng chính:

- `evidence/02-dvc-cloud-storage.png`
- `evidence/04-eval-gate-failed-0.68.png`
- `evidence/05-vm-api.png`
- `evidence/06-github-actions-success.png`
- `evidence/07-github-actions-step3-data-trigger.png`
- `evidence/07-model-cloud-storage.png`

## 5. Kết luận

Bài lab đã hoàn thiện quy trình từ tracking experiment, versioning dữ liệu, CI/CD quality gate đến triển khai model liên tục trên VM. Eval gate bảo đảm model chưa đạt accuracy 0.70 không được triển khai; sau khi bổ sung dữ liệu, model đạt 0.75 và được deploy tự động thành công.

Các cảnh báo Node.js trong GitHub Actions chỉ là cảnh báo deprecation của action dependency, không ảnh hưởng đến kết quả pipeline. Ảnh MLflow hiện có chứng minh việc ghi params/metrics cho các run; phần comparison UI giữa các hyperparameters chưa được bổ sung riêng trong bộ ảnh nộp.
