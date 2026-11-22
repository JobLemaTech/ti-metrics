from src.parsers.csv_parser import CSVLogParser
from src.parsers.json_parser import JSONLogParser
from src.services.analysis import LogAnalyzer
from src.services.geolocation import GeolocationClient
from src.services.metrics_application import MetricsApplication
from src.utils.report import JSONReportWriter


def main():
    parsers = [
        CSVLogParser("data/logs.csv"),
        JSONLogParser("data/events.json"),
    ]
    analyzer = LogAnalyzer()
    geolocation_client = GeolocationClient()
    report_writer = JSONReportWriter("output/report.json")

    application = MetricsApplication(
        parsers=parsers,
        analyzer=analyzer,
        geolocation_client=geolocation_client,
        report_writer=report_writer,
    )

    try:
        report = application.run()
    except (ValueError, OSError) as error:
        print(f"No se pudo completar el procesamiento: {error}")
        return

    print(f"Reporte generado en {report_writer.output_path}")
    print("Métricas:", report["metrics"])
    print("Geolocalización:", report["geolocation"])


if __name__ == "__main__":
    main()