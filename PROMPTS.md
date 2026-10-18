# Bitácora de co-programación con IA

## Registro de Prompt #1

* **Fecha:** 2026-10-17
* **Módulo/Función:** Lectura CSV/JSON, validación, deduplicación, métricas, geolocalización y reporte del Hito 1.
* **Prompt Enviado:** “Ayúdame a realizar el Hito 1 paso a paso. Quiero escribir yo el código y entender para qué sirve cada parte.”
* **Respuesta de la IA:** Guió la construcción incremental de `read_csv_logs` con `csv.DictReader`, `read_json_events` con `json.load`, `normalize_event` para convertir y validar campos, `deduplicate_events` usando una tupla y un conjunto, y `calculate_metrics` para HTTP 500 e IPs críticas. También orientó la integración de `requests` con ip-api.com y la escritura de `output/report.json`. Ejemplos de código sugeridos: `normalized["status"] = int(normalized["status"])`, `seen_events = set()` y `requests.get(url, params=params, timeout=5)`.
* **Análisis Crítico:** Se corrigieron nombres de variables inconsistentes antes de ejecutar el código. Se agregó manejo de registros inválidos y errores de lectura. La geolocalización es aproximada; además, el endpoint gratuito de ip-api.com tiene límites de solicitudes, así que consultar muchas IPs distintas puede requerir controlar la frecuencia.
* **Solución Final Aplicada:** Escribí los módulos en `src/parsers/`, `src/services/`, `src/utils/` y el punto de entrada `main.py`. Comprobé manualmente la lectura de CSV/JSON, la conversión de tipos, el descarte de una IP inválida, la deduplicación de tres registros a dos, el cálculo de 50 % de errores HTTP 500 y la generación de `output/report.json`.

## Registro de Prompt #2

* **Fecha:** 2026-10-18
* **Módulo/Función:** `README.md`, documentación del Hito 1.
* **Prompt Enviado:** Compartí el contenido actual de mi README y pedí orientación para documentar la instalación, ejecución y decisiones del Hito 1, avanzando despacio.
* **Respuesta de la IA:** Propuso agregar una sección con los requisitos, los comandos para instalar dependencias y ejecutar `main.py`, la ubicación del reporte y las reglas de cálculo y deduplicación.
* **Análisis Crítico:** El primer ejemplo del bloque de comandos se formateó de manera confusa por el anidamiento de bloques Markdown. Se corrigió y se aclaró que `powershell` es una etiqueta opcional de formato, no un comando que se ejecuta.
* **Solución Final Aplicada:** Agregué al README la sección del Hito 1, las instrucciones de instalación y ejecución en Windows, la ruta `output/report.json` y las decisiones de métricas y validación.