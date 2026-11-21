from abc import ABC, abstractmethod
from pathlib import Path

class BaseLogParser(ABC):
    def __init__(self, path):
        self._path = Path(path)

    @property
    def path(self):
        return self._path

    @abstractmethod
    def read(self):
        """Lee el archivo y devuelve una lista de eventos."""
