import json
from src.parsers.base_parser import BaseLogParser


class JSONLogParser(BaseLogParser):
    def read(self):
        try:
            with self.path.open("r", encoding="utf-8") as file:
                events = json.load(file)
        except (OSError, json.JSONDecodeError) as exc:
            raise ValueError(f"No se pudo leer el JSON '{self.path}': {exc}") from exc
        if not isinstance(events, list):
            raise ValueError("El JSON debe contener una lista de eventos.")
        for event in events:
            if not isinstance(event, dict):
                raise ValueError("Cada evento del JSON debe ser un objeto.")
        return events