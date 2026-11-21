class LogEvent:
    def __init__(self, timestamp, ip, method, path, status, cpu_percent, memory_percent):
        self._timestamp = timestamp
        self._ip = ip
        self._method = method
        self._path = path
        self._status = status
        self._cpu_percent = cpu_percent
        self._memory_percent = memory_percent

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def ip(self):
        return self._ip

    @property
    def method(self):
        return self._method

    @property
    def path(self):
        return self._path

    @property
    def status(self):
        return self._status

    @property
    def cpu_percent(self):
        return self._cpu_percent

    @property
    def memory_percent(self):
        return self._memory_percent

    @property
    def is_http_500(self):
        return self.status == 500

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "ip": self.ip,
            "method": self.method,
            "path": self.path,
            "status": self.status,
            "cpu_percent": self.cpu_percent,
            "memory_percent": self.memory_percent,
        }

    def deduplication_key(self):
        return (
            self.timestamp,
            self.ip,
            self.method,
            self.path,
            self.status,
            self.cpu_percent,
            self.memory_percent,
        )