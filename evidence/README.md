# Evidence checklist

Các minh chứng local đã được ghi trong [`local_validation.md`](local_validation.md). Browser trong phiên làm việc không có tab/runtime khả dụng, và repo không có credential cloud, nên chưa thể tạo screenshot MLflow/GitHub/GCS/VM thật.

Cần bổ sung các ảnh sau sau khi chạy trên tài khoản của bạn:

1. `01-mlflow-three-runs.png`: MLflow UI, tối thiểu 3 runs, params, accuracy và f1_score.
2. `02-dvc-cloud-storage.png`: Cloud Storage hiển thị dữ liệu dưới `dvc/`.
3. `03-github-actions-step2.png`: bốn jobs Bước 2 màu xanh.
4. `04-vm-api.png`: terminal chứa kết quả `/health` và `/predict`.
5. `05-model-cloud-storage.png`: `models/latest/model.pkl` trên bucket.
6. `06-github-actions-step3-data-trigger.png`: pipeline được kích hoạt bởi commit file `.dvc`, đủ bốn jobs xanh.

Không chụp hoặc commit service-account JSON, private SSH key, GitHub Secret hay dữ liệu CSV nếu đã được DVC quản lý.
