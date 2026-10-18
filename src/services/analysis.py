from ipaddress import ip_address

REQUIRED_FIELDS = (
    "timestamp",
    "ip",
    "method",
    "path",
    "status",
    "cpu_percent",
    "memory_percent",
)
def normalize_event(event):
    for field in REQUIRED_FIELDS:
        if field not in event or event[field] in (None, ""):
            return None
    normalized = event.copy()
    try:
        normalized["status"] = int(normalized["status"])
        normalized["cpu_percent"] = float(normalized["cpu_percent"])
        normalized["memory_percent"] = float(normalized["memory_percent"])
    except (TypeError, ValueError):
        return None
    try:
        ip_address(normalized["ip"])
    except (ValueError, TypeError):
        return None
    if not 100 <= normalized["status"] <= 599:
        return None
    if not 0 <= normalized["cpu_percent"] <= 100:
        return None
    if not 0 <= normalized["memory_percent"] <= 100:
        return None
    return normalized
def deduplicate_events(events):
    unique_events = []
    seen_events = set()
    for event in events:
        normalized = normalize_event(event)
        if normalized is None:
            continue
        event_key = (
            normalized["timestamp"],
            normalized["ip"],
            normalized["method"],
            normalized["path"],
            normalized["status"],
            normalized["cpu_percent"],
            normalized["memory_percent"],
        )
        if event_key not in seen_events:
            seen_events.add(event_key)
            unique_events.append(normalized)
    return unique_events
def calculate_metrics(events):
    total_events = len(events)
    errors_500 = []
    for event in events:
        if event["status"] == 500:
            errors_500.append(event)
    if total_events > 0:
        error_percentage = (len(errors_500) / total_events) * 100
    else:
        error_percentage = 0

    critical_ips = set()
    for event in errors_500:
        critical_ips.add(event["ip"])
    return {
        "total_events": total_events,
        "http_500_count": len(errors_500),
        "http_500_percentage": round(error_percentage, 2),
        "critical_ips": sorted(critical_ips),
    }
