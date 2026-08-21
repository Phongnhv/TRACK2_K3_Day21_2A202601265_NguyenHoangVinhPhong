from pathlib import Path

import yaml


workflow = Path(__file__).parents[1] / ".github" / "workflows" / "mlops.yml"
with workflow.open(encoding="utf-8") as stream:
    document = yaml.safe_load(stream)

assert document["name"] == "MLOps Pipeline"
assert len(document["jobs"]) == 4
assert set(document["jobs"]) == {"test", "train", "eval", "deploy"}
print("Workflow YAML parsed; four jobs found.")
