import csv
from src.parsers.base_parser import BaseLogParser

class CSVLogParser(BaseLogParser):
    def read(self):
        try:
            with self.path.open("r", encoding="utf-8", newline="") as file:
                reader = csv.DictReader(file)
                return list(reader)
        except OSError as exc:
            raise ValueError(f"No se pudo leer el CSV '{self.path}': {exc}") from exc
