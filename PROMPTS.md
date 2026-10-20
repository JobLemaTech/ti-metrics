# Bitácora de co-programación con IA

## Registro de Prompt #1

* **Fecha:** 2026-10-17
* **Módulo/Función:** Lectura CSV/JSON, validación, deduplicación, métricas, geolocalización y reporte del Hito 1.
* **Prompt Enviado:** “Ayúdame a realizar el Hito 1 paso a paso. Quiero escribir yo el código y entender para qué sirve cada parte.”
* **Respuesta de la IA:** Guió la construcción incremental de `read_csv_logs` con `csv.DictReader`, `read_json_events` con `json.load`, `normalize_event` para convertir y validar campos, `deduplicate_events` usando una tupla y un conjunto, y `calculate_metrics` para HTTP 500 e IPs críticas. También orientó la integración de `requests` con ip-api.com y la escritura de `output/report.json`. Ejemplos de código sugeridos: `normalized["status"] = int(normalized["status"])`, `seen_events = set()` y `requests.get(url, params=params, timeout=5)`.
* **Análisis Crítico:** Se corrigieron nombres de variables inconsistentes antes de ejecutar el código. Se agregó manejo de registros inválidos y errores de lectura. La geolocalización es aproximada; además, el endpoint gratuito de ip-api.com tiene límites de solicitudes, así que consultar muchas IPs distintas puede requerir controlar la frecuencia.
* **Solución Final Aplicada:** Escribí los módulos en `src/parsers/`, `src/services/`, `src/utils/` y el punto de entrada `main.py`. Comprobé manualmente la lectura de CSV/JSON, la conversión de tipos, el descarte de una IP inválida, la deduplicación de tres registros a dos, el cálculo de 50 % de errores HTTP 500 y la generación de `output/report.json`.

## Registro de Prompt #2

* **Fecha:** 2026-10-17
* **Módulo/Función:** `README.md`, documentación del Hito 1.
* **Prompt Enviado:** Compartí el contenido actual de mi README y pedí orientación para documentar la instalación, ejecución y decisiones del Hito 1, avanzando despacio.
* **Respuesta de la IA:** Propuso agregar una sección con los requisitos, los comandos para instalar dependencias y ejecutar `main.py`, la ubicación del reporte y las reglas de cálculo y deduplicación.
* **Análisis Crítico:** El primer ejemplo del bloque de comandos se formateó de manera confusa por el anidamiento de bloques Markdown. Se corrigió y se aclaró que `powershell` es una etiqueta opcional de formato, no un comando que se ejecuta.
* **Solución Final Aplicada:** Agregué al README la sección del Hito 1, las instrucciones de instalación y ejecución en Windows, la ruta `output/report.json` y las decisiones de métricas y validación.

## Registro de Prompt #3

* **Fecha:** 2026-10-17
* **Módulo/Función:** Estructura inicial del proyecto y control de versiones.
* **Prompt Enviado:** [Reconstruido] “¿Cómo organizo las carpetas para el Hito 1 y cómo compruebo que Git ignore `.venv`?”
* **Respuesta de la IA:** Explicó la estructura del repositorio, el uso de `.gitignore` y el comando `git check-ignore -v` para verificar que `.venv` no se agregue a Git.
* **Análisis Crítico:** La salida de `git check-ignore` debía leerse con cuidado porque se confundieron visualmente las líneas de `.venv` y `venv/`. La comprobación confirmó que `.venv` sí estaba ignorada.
* **Solución Final Aplicada:** Se mantuvo `.venv` fuera del control de versiones y se continuó trabajando dentro del entorno virtual.

## Registro de Prompt #4

* **Fecha:** 2026-10-17
* **Módulo/Función:** `src/parsers/csv_parser.py` — lectura de CSV.
* **Prompt Enviado:** [Reconstruido] “¿Cómo leo los registros de `logs.csv` como diccionarios y manejo errores al abrir el archivo?”
* **Respuesta de la IA:** Orientó el uso de `Path`, `csv.DictReader`, `encoding="utf-8"` y `newline=""`. También explicó cómo convertir un error de lectura en un mensaje entendible.
* **Análisis Crítico:** Al principio se usó un nombre de variable distinto al parámetro de la función (`paths` frente a `path`). Se corrigió antes de continuar.
* **Solución Final Aplicada:** Implementé `read_csv_logs(path)` y comprobé que devolviera los registros del archivo como una lista de diccionarios.

## Registro de Prompt #5

* **Fecha:** 2026-10-17
* **Módulo/Función:** `src/parsers/json_parser.py` — lectura y validación de JSON.
* **Prompt Enviado:** [Reconstruido] “¿Cómo leo `events.json` y compruebo que tenga una lista de eventos, donde cada evento sea un objeto?”
* **Respuesta de la IA:** Explicó el uso de `json.load`, el manejo de errores de archivo y JSON inválido, y las comprobaciones del tipo de los datos.
* **Análisis Crítico:** Una versión inicial puso la validación dentro del bloque `except` y otra tenía el `return` dentro del ciclo. Eso podía impedir validar correctamente todos los eventos. Se reorganizó el flujo.
* **Solución Final Aplicada:** La función carga el JSON, convierte errores de lectura o formato en `ValueError`, verifica que la raíz sea una lista y que cada elemento sea un diccionario, y luego devuelve la lista.

## Registro de Prompt #6

* **Fecha:** 2026-10-17
* **Módulo/Función:** `src/services/analysis.py` — normalización y deduplicación.
* **Prompt Enviado:** [Reconstruido] “¿Cómo convierto los campos numéricos y uso una tupla y un conjunto para eliminar eventos duplicados?”
* **Respuesta de la IA:** Explicó la conversión de `status`, `cpu_percent` y `memory_percent`, y cómo formar una clave inmutable para registrarla en un conjunto.
* **Análisis Crítico:** En un primer intento se usaron nombres de variables inconsistentes dentro de la función. Además, el orden de normalizar antes de comparar evita que, por ejemplo, `500` y `"500"` se traten como valores distintos.
* **Solución Final Aplicada:** Implementé `normalize_event` y `deduplicate_events`. La clave de duplicación incluye timestamp, IP, método, ruta, estado HTTP, CPU y memoria. Comprobé que tres entradas se redujeran a dos eventos únicos.

## Registro de Prompt #7

* **Fecha:** 2026-10-17
* **Módulo/Función:** `src/services/analysis.py` — validación de eventos y métricas.
* **Prompt Enviado:** [Reconstruido] “¿Cómo descarto eventos incompletos o inválidos y calculo el porcentaje de errores HTTP 500 y las IPs críticas?”
* **Respuesta de la IA:** Orientó la validación de campos obligatorios, conversiones numéricas, validación de IP y rangos. También explicó contar errores 500 y obtener las IPs críticas sin duplicados.
* **Análisis Crítico:** Se detectó un nombre de variable incorrecto en el cálculo de métricas (`errors_500` en vez de la lista creada). También había que considerar el caso de cero eventos para evitar dividir entre cero.
* **Solución Final Aplicada:** Los eventos inválidos se descartan; el porcentaje se calcula sobre los eventos válidos sin duplicados. Se acordó que una IP es crítica cuando tiene al menos un evento con estado 500.

## Registro de Prompt #8

* **Fecha:** 2026-10-17
* **Módulo/Función:** `src/services/geolocation.py` — consulta de API REST.
* **Prompt Enviado:** [Reconstruido] “¿Cómo consulto una API de geolocalización para cada IP y manejo errores de conexión?”
* **Respuesta de la IA:** Explicó el uso de `requests.get`, parámetros de consulta, tiempo límite (`timeout`) y manejo de errores de red o de respuesta JSON.
* **Análisis Crítico:** La ubicación asociada a una IP es aproximada. La API puede fallar o limitar solicitudes, así que el programa no debe asumir que todas las respuestas serán exitosas.
* **Solución Final Aplicada:** Implementé `get_ip_geolocation` y `enrich_ips`; esta última consulta IPs únicas y guarda los resultados por dirección IP. Probé la consulta con las IPs de ejemplo.

## Registro de Prompt #9

* **Fecha:** 2026-10-18
* **Módulo/Función:** `src/utils/report.py` y `main.py` — integración y reporte.
* **Prompt Enviado:** [Reconstruido] “¿Cómo uno los lectores, el análisis y la geolocalización, y guardo el resultado como JSON?”
* **Respuesta de la IA:** Orientó la integración desde `main.py` y el uso de `json.dump` para guardar el reporte, creando antes la carpeta de salida si no existía.
* **Análisis Crítico:** Había que mantener separado el análisis de eventos de la escritura del archivo y contemplar errores de lectura. También comprobé que el reporte generado fuera JSON válido.
* **Solución Final Aplicada:** Implementé `write_report` y conecté las funciones desde `main.py`. El programa genera `output/report.json` con las métricas y la geolocalización.

## Registro de Prompt #10

* **Fecha:** 2026-10-18
* **Módulo/Función:** `README.md` y publicación del Hito 1 en GitHub.
* **Prompt Enviado:** [Reconstruido] “¿Qué debe incluir el README para explicar cómo instalar y ejecutar el Hito 1, y cómo subo los archivos a GitHub?”
* **Respuesta de la IA:** Orientó la documentación de requisitos, comandos de ejecución y decisiones de análisis. Después explicó cómo revisar los cambios, crear un commit semántico y subirlos a la rama `main`.
* **Análisis Crítico:** Se corrigió el formato del bloque de comandos de PowerShell en el README. Antes de publicar, comprobé qué archivos estaban preparados para el commit y que `.venv` no apareciera.
* **Solución Final Aplicada:** Actualicé el README, registré la asistencia en esta bitácora y publiqué los cambios del Hito 1. Verifiqué que Git indicara la rama sincronizada y el árbol de trabajo limpio.

## Registro de Prompt #11

* **Fecha:** 2026-10-20
* **Módulo/Función:** `README.md` — documentación de uso y alcance del Hito 1.
* **Prompt Enviado:** [Reconstruido] “¿Qué información puedo añadir al README para que el usuario entienda qué archivos necesita, qué reporte genera y qué incluye el Hito 1?”
* **Respuesta de la IA:** Sugirió explicar los campos esperados en los eventos, el contenido del reporte, el comportamiento ante fallos de geolocalización y el alcance de esta entrega.
* **Análisis Crítico:** Debía comprobar que las rutas y el comportamiento descritos coincidieran con el proyecto real. También se aclaró que el README es una guía de uso y documentación, no una interfaz gráfica.
* **Solución Final Aplicada:** Amplié el README con información para entender los datos de entrada, el reporte JSON y el alcance de esta versión del proyecto.

## Registro de Prompt #12

* **Fecha:** 2026-10-20
* **Módulo/Función:** `data/logs.csv` y `README.md` — ampliación de datos de ejemplo y documentación de resultados.
* **Prompt Enviado:** [Reconstruido] “¿Conviene agregar más eventos para explicar mejor el análisis y cómo documento los resultados?”
* **Respuesta de la IA:** Recomendó agregar eventos variados con estados HTTP `200`, `401`, `404` y `500`, mantener un duplicado entre los archivos y explicar los resultados obtenidos.
* **Análisis Crítico:** Había que comprobar que los eventos nuevos tuvieran los campos requeridos y valores válidos, conservar el duplicado para demostrar la deduplicación y volver a ejecutar el programa para obtener métricas reales.
* **Solución Final Aplicada:** Añadí seis eventos al CSV, ejecuté el programa y comprobé que procesara 8 eventos únicos, con 3 errores HTTP 500 (37,5 %) y `1.1.1.1` como IP crítica. Actualicé el README para documentar esos resultados.