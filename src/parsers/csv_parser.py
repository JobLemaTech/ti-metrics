import csv
from pathlib import Path

def read_csv_logs(path):
    file_path = Path(path)
    try:
        with file_path.open("r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except OSError as exc:
        raise ValueError(f"No se pudo leer el CSV '{file_path}': {exc}") from exc