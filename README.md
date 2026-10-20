# 🚀 TI-Metrics: Engine de Analítica de Logs

**Asignatura:** Programación II  
**Estudiante:** Job Lema  
**Carrera:** Ingeniería en Tecnologías de la Información

## 🏆 Cuadro de Logros y Badges

| Badge | Estado | Hito Asociado |
| :--- | :---: | :--- |
| **Data Wrangler** | ![Data Wrangler](https://img.shields.io/badge/Data_Wrangler-Bloqueado-inactive?style=for-the-badge&logo=python) | Hito 1: Persistencia & APIs |
| **OOP Architect** | ![OOP Architect](https://img.shields.io/badge/OOP_Architect-Bloqueado-inactive?style=for-the-badge&logo=diagrams.net) | Hito 2: Arquitectura POO |
| **PyTest Guardian** | ![PyTest Guardian](https://img.shields.io/badge/PyTest_Guardian-Bloqueado-inactive?style=for-the-badge&logo=pytest) | Hito 3: Cobertura > 80% |
| **AI Auditor** | ![AI Auditor](https://img.shields.io/badge/AI_Auditor-Bloqueado-inactive?style=for-the-badge&logo=openai) | Hito 3: PROMPTS.md & TDD |
| **Git Flow Master** | ![Git Flow Master](https://img.shields.io/badge/Git_Flow_Master-Bloqueado-inactive?style=for-the-badge&logo=github) | Transversal: Commits Semánticos |

## Hito 1: Persistencia y APIs

TI-Metrics lee registros desde `data/logs.csv` y `data/events.json`, valida los campos, normaliza los valores numéricos, elimina eventos duplicados y calcula métricas HTTP. También consulta una API geográfica para las IPs únicas.

### Requisitos

- Python 3 instalado.
- Conexión a internet para consultar la geolocalización.
- Dependencias instaladas desde `requirements.txt`.

### Instalación y ejecución en Windows

Desde la carpeta raíz del proyecto, ejecuta:

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

El programa lee `data/logs.csv` y `data/events.json`. Crea la carpeta `output` si no existe y guarda el reporte en `output/report.json`.

### Métricas y decisiones

- El porcentaje HTTP 500 se calcula sobre los eventos válidos después de eliminar duplicados.
- Una IP se considera crítica si tiene al menos un evento con estado HTTP 500.
- Dos registros se consideran duplicados si coinciden en timestamp, IP, método, ruta, estado HTTP, CPU y memoria.
- Se descartan registros con campos incompletos, IP inválida o valores numéricos fuera de rango.
- La geolocalización es una estimación asociada a la IP.

### Resultados con los datos de ejemplo

| Indicador | Resultado |
| :--- | ---: |
| Eventos del CSV | 8 |
| Eventos del JSON | 1 |
| Registros duplicados | 1 |
| Eventos válidos y únicos analizados | 8 |
| Errores HTTP 500 | 3 |
| Porcentaje de errores HTTP 500 | 37,5 % |
| IP crítica | `1.1.1.1` |

El evento del JSON ya está presente en el CSV, por eso se elimina como duplicado. La geolocalización se consulta para las IPs únicas y puede variar según la respuesta del servicio.

### Formato de los archivos de entrada

Cada evento debe incluir estos campos:

- `timestamp`: fecha y hora del evento.
- `ip`: dirección IP.
- `method`: método HTTP, por ejemplo, `GET` o `POST`.
- `path`: ruta solicitada, por ejemplo, `/health`.
- `status`: estado HTTP, como `200` o `500`.
- `cpu_percent`: porcentaje de uso de CPU entre 0 y 100.
- `memory_percent`: porcentaje de uso de memoria entre 0 y 100.

El archivo CSV debe tener una fila de encabezados con esos nombres. El archivo JSON debe contener una lista de eventos, donde cada evento sea un objeto con esos campos. Los registros incompletos o con valores inválidos se excluyen del análisis.

### Reporte generado

El programa crea `output/report.json`. El reporte contiene:

- `total_events`: cantidad de eventos válidos y únicos.
- `http_500_count`: cantidad de eventos con estado HTTP 500.
- `http_500_percentage`: porcentaje de errores HTTP 500.
- `critical_ips`: direcciones IP que tuvieron al menos un error HTTP 500.
- `geolocation`: información geográfica consultada para cada IP única.

Con los datos de ejemplo, el análisis produce 2 eventos válidos y únicos y 1 error HTTP 500, equivalente al 50 %. Los resultados pueden cambiar si se modifican los archivos de entrada.

La geolocalización depende de una API externa y de una conexión a internet. La ubicación es aproximada; si la consulta falla, el reporte incluye el estado y el mensaje del error.

## Alcance de esta entrega

Esta versión corresponde al Hito 1 de TI-Metrics e incluye la lectura de archivos CSV y JSON, la validación y deduplicación de eventos, el cálculo de métricas, la consulta de geolocalización y la generación del reporte JSON.