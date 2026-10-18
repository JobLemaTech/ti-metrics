from src.parsers.csv_parser import read_csv_logs
from src.parsers.json_parser import read_json_events
from src.services.analysis import deduplicate_events, calculate_metrics
from src.services.geolocation import enrich_ips
from src.utils.report import write_report

def main():
    try:
        csv_events = read_csv_logs("data/logs.csv")
        json_events = read_json_events("data/events.json")
    except ValueError as error:
        print(f"No se pudo procesar los archivos: {error}")
        return
    all_events = csv_events + json_events
    unique_events = deduplicate_events(all_events)
    metrics = calculate_metrics(unique_events)
    ip_addresses = {event["ip"] for event in unique_events}
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