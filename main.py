from src.services.analysis import deduplicate_events, calculate_metrics
from src.services.geolocation import enrich_ips
from src.utils.report import write_report
from src.parsers.csv_parser import CSVLogParser
from src.parsers.json_parser import JSONLogParser

def main():
    try:
        csv_parser = CSVLogParser("data/logs.csv")
        json_parser = JSONLogParser("data/events.json")
        parsers = [csv_parser, json_parser]
        all_events = []
        for parser in parsers:
            all_events += parser.read()
    except ValueError as error:
        print(f"No se pudo procesar los archivos: {error}")
        return
    unique_events = deduplicate_events(all_events)
    metrics = calculate_metrics(unique_events)
    ip_addresses = {event.ip for event in unique_events}
    geolocation = enrich_ips(ip_addresses)
    report = {
        "metrics": metrics,
        "geolocation": geolocation,
    }
    write_report(report, "output/report.json")
    print("Reporte generado en output/report.json")
    print("Métricas:", metrics)
    print("Geolocalización:", geolocation)
if __name__ == "__main__":
    main()