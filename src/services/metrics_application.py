class MetricsApplication:
    def __init__(self, parsers, analyzer, geolocation_client, report_writer):
        self._parsers = parsers
        self._analyzer = analyzer
        self._geolocation_client = geolocation_client
        self._report_writer = report_writer
    def run(self):
        all_events = []
        for parser in self._parsers:
            all_events.extend(parser.read())

        unique_events = self._analyzer.deduplicate_events(all_events)
        metrics = self._analyzer.calculate_metrics(unique_events)
        ip_addresses = {event.ip for event in unique_events}
        geolocation = self._geolocation_client.enrich_ips(ip_addresses)
        report = {"metrics": metrics, "geolocation": geolocation}
        self._report_writer.write(report)
        return report
