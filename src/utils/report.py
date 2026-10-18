import json
from pathlib import Path

def write_report(report, output_path):
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)