# Evidence checklist

Các minh chứng local đã được ghi trong [`local_validation.md`](local_validation.md). Ảnh `04-eval-gate-failed-0.68.png` đã được lưu trong repo và chứng minh quality gate Bước 2 chặn model có accuracy 0.68.

Cần bổ sung các ảnh sau sau khi chạy trên tài khoản của bạn:

1. `01-mlflow-three-runs.png`: MLflow UI, tối thiểu 3 runs, params, accuracy và f1_score.
2. `02-dvc-cloud-storage.png`: Cloud Storage hiển thị dữ liệu dưới `dvc/`.
3. `03-github-actions-step2.png`: bốn jobs Bước 2 màu xanh.
4. `04-eval-gate-failed-0.68.png`: GitHub Actions hiển thị Eval fail ở accuracy 0.6800 < 0.70; Deploy bị chặn đúng thiết kế.
5. `05-vm-api.png`: terminal chứa kết quả `/health` và `/predict`.
6. `06-model-cloud-storage.png`: `models/latest/model.pkl` trên bucket.
7. `07-github-actions-step3-data-trigger.png`: pipeline được kích hoạt bởi commit file `.dvc`, đủ bốn jobs xanh.

Không chụp hoặc commit service-account JSON, private SSH key, GitHub Secret hay dữ liệu CSV nếu đã được DVC quản lý.
