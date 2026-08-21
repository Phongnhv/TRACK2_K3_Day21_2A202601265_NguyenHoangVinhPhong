# Báo cáo Lab MLOps Day 21 — Wine Quality

## 1. Mục tiêu

Xây dựng quy trình MLOps từ huấn luyện cục bộ đến CI/CD: theo dõi thí nghiệm bằng MLflow, quản lý dữ liệu bằng DVC, kiểm tra chất lượng qua GitHub Actions và phục vụ model bằng FastAPI trên Cloud VM.

## 2. Kết quả triển khai

- Hoàn thiện `src/train.py`: đọc dữ liệu, train Random Forest, log params/metrics/model lên MLflow, tạo `outputs/metrics.json` và `models/model.pkl`.
- Hoàn thiện unit tests trong `tests/test_train.py`.
- Hoàn thiện `src/serve.py` với `/health` và `/predict`, kiểm tra đúng 12 features.
- Hoàn thiện workflow 4 jobs: Unit Test → Train → Eval → Deploy.
- Khởi tạo DVC, tạo pointer cho ba dataset và cấu hình remote GCS `gs://vinuni-lab16-phong-2026-mlops/dvc`; credential được lấy từ GitHub Secrets/local ignored config, không lưu trong Git.

## 3. Thí nghiệm và đánh giá

| Run | n_estimators | max_depth | min_samples_split | Accuracy | F1 weighted |
|---:|---:|---:|---:|---:|---:|
| 1 | 100 | 5 | 2 | 0.5640 | 0.5534 |
| 2 | 50 | 3 | 2 | 0.5580 | 0.5185 |
| 3 | 200 | 10 | 5 | 0.6440 | 0.6417 |
| 4 — tốt nhất | 500 | None | 5 | 0.6800 | 0.6786 |

Cấu hình tốt nhất được lưu trong `params.yaml`. Tăng số cây và bỏ giới hạn độ sâu giúp model biểu diễn tốt hơn trên tập đánh giá, nhưng với đúng 2998 mẫu của Bước 2 accuracy thực tế vẫn dưới ngưỡng CI `0.70`; eval gate vì vậy phải chặn deploy, đúng thiết kế an toàn.

Khi mô phỏng Bước 3 bằng cách gộp thêm 2998 mẫu (`2998 → 5996`), cùng cấu hình đạt `accuracy=0.7500`, `f1_score=0.7486`, vượt eval gate.

## 4. Kiểm thử

- `pytest tests/ -v`: **3 passed**.
- `python -m compileall -q src tests generate_data.py add_new_data.py`: đạt.
- `dvc status`: **Data and pipelines are up to date.**
- FastAPI local smoke test: `/health` trả `{"status":"ok"}`; `/predict` trả `{"prediction":0,"label":"thap"}` với request 12 features.

## 5. Kết luận và minh chứng cloud

Phần code, unit test, MLflow, DVC metadata, workflow và API đã được hoàn thiện trong repo. DVC đã push thành công dữ liệu B2 và dữ liệu B3 lên bucket GCS. Lần chạy GitHub Actions B2 xác nhận Unit Test và Train đạt, còn Eval chặn accuracy 0.6800; ảnh minh chứng được lưu tại `evidence/04-eval-gate-failed-0.68.png`.

Sau khi thêm dữ liệu B3, pointer `data/train_phase1.csv.dvc` đã đổi sang phiên bản 5996 mẫu và object mới đã được `dvc push` lên GCS. Kết quả local tương ứng là accuracy 0.7500 và weighted F1 0.7486, đủ vượt gate 0.70. Pipeline GitHub Actions chạy thành công cả bốn jobs `Unit Test → Train → Eval → Deploy`. API trên VM trả kết quả `/predict` hợp lệ và GCS hiển thị `models/latest/model.pkl`.

Các minh chứng cloud được lưu trong thư mục `evidence/`: `05-vm-api.png`, `06-github-actions-success.png` và `07-model-cloud-storage.png`. Ảnh quality gate Bước 2 bị chặn đúng ngưỡng được lưu tại `04-eval-gate-failed-0.68.png`.
