# Evidence checklist

Các minh chứng local đã được ghi trong [`local_validation.md`](local_validation.md). Các ảnh cloud đã có trong repo gồm `02-dvc-cloud-storage.png`, `04-eval-gate-failed-0.68.png`, `05-vm-api.png`, `06-github-actions-success.png`, `07-github-actions-step3-data-trigger.png` và `07-model-cloud-storage.png`.

Minh chứng còn thiếu hoặc cần bổ sung:

1. `01-mlflow-three-runs.png`: MLflow UI dạng danh sách/comparison, tối thiểu 3 runs với hyperparameters khác nhau, accuracy và f1_score.
   Hiện có `01-mlflow-run-1.png`, `01-mlflow-run-2.png`, `01-mlflow-run-3.png`; cả ba đang hiển thị cùng `n_estimators=10`, `max_depth=3`, nên chỉ là minh chứng log run, chưa đủ chứng minh thí nghiệm khác nhau.
2. `02-dvc-cloud-storage.png`: Cloud Storage hiển thị dữ liệu dưới `dvc/` — **đã có**.
3. `03-github-actions-step2.png`: bốn jobs Bước 2 màu xanh (có thể dùng ảnh `06-github-actions-success.png` nếu bài nộp không yêu cầu tách riêng Bước 2).
4. `04-eval-gate-failed-0.68.png`: GitHub Actions hiển thị Eval fail ở accuracy 0.6800 < 0.70; Deploy bị chặn đúng thiết kế.
5. `05-vm-api.png`: terminal chứa kết quả `/health` và `/predict`.
6. `06-github-actions-success.png`: bốn jobs xanh trong lần chạy thành công.
7. `07-model-cloud-storage.png`: `models/latest/model.pkl` trên bucket — **đã có**.

Ảnh `07-github-actions-step3-data-trigger.png` đã xác nhận commit `4001541`, sự kiện `push` và cả bốn jobs xanh; vì vậy objective tự động hóa Bước 3 đã có minh chứng hợp lệ.

Không chụp hoặc commit service-account JSON, private SSH key, GitHub Secret hay dữ liệu CSV nếu đã được DVC quản lý.
