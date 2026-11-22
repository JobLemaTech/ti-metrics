import json
from pathlib import Path

class JSONReportWriter:
    def __init__(self, output_path):
        self._output_path = Path(output_path)

    @property
    def output_path(self):
        return self._output_path

    def write(self, report):
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        with self.output_path.open("w", encoding="utf-8") as file:
            json.dump(report, file, indent=4, ensure_ascii=False)