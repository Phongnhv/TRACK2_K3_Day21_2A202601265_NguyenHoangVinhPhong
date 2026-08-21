# Evidence checklist

Các minh chứng local đã được ghi trong [`local_validation.md`](local_validation.md). Các ảnh cloud đã có trong repo gồm `04-eval-gate-failed-0.68.png`, `05-vm-api.png`, `06-github-actions-success.png` và `07-model-cloud-storage.png`.

Minh chứng còn thiếu hoặc cần bổ sung:

1. `01-mlflow-three-runs.png`: MLflow UI, tối thiểu 3 runs, params, accuracy và f1_score.
2. `02-dvc-cloud-storage.png`: Cloud Storage hiển thị dữ liệu dưới `dvc/`.
3. `03-github-actions-step2.png`: bốn jobs Bước 2 màu xanh (có thể dùng ảnh `06-github-actions-success.png` nếu bài nộp không yêu cầu tách riêng Bước 2).
4. `04-eval-gate-failed-0.68.png`: GitHub Actions hiển thị Eval fail ở accuracy 0.6800 < 0.70; Deploy bị chặn đúng thiết kế.
5. `05-vm-api.png`: terminal chứa kết quả `/health` và `/predict`.
6. `06-github-actions-success.png`: bốn jobs xanh trong lần chạy thành công.
7. `07-model-cloud-storage.png`: `models/latest/model.pkl` trên bucket.

Lưu ý: ảnh `06-github-actions-success.png` là lần chạy thủ công (`workflow_dispatch`). Để chứng minh tuyệt đối yêu cầu Bước 3, cần re-run workflow `data-phase2` trước đó sau khi đã thêm VM secrets; lần chạy đó phải giữ commit `4001541` và sự kiện push dữ liệu.

Không chụp hoặc commit service-account JSON, private SSH key, GitHub Secret hay dữ liệu CSV nếu đã được DVC quản lý.
