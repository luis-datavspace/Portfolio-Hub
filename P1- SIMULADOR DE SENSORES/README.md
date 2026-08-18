# 🏭 Simulador de Pipeline de Datos de Fábrica


---

## Descripción

Proyecto personal que simula un **pipeline de datos industrial** usando Python orientado a objetos.

El programa simula sensores de una fábrica que envían lecturas de temperatura y presión. Un sistema central (Monitor) recibe esos datos, los valida, detecta anomalías y genera un reporte del estado de la fábrica — tanto en consola como en archivo `.txt`.

Construido como **primer proyecto real** fuera de ejercicios básicos, aplicando principios reales de Data Engineering.

---

## Conceptos aplicados

| Concepto | Descripción |
|---|---|
| **POO** | Clases, atributos, métodos, instancias |
| **Validación en la ingesta** | Detección de datos corruptos antes de procesarlos |
| **Fuente única de verdad** | Los límites de los sensores viven en un solo lugar |
| **Pipeline por etapas** | Ingesta → Filtrado → Reporte |
| **Manejo de datos sucios** | Lecturas inválidas se marcan y conservan, no se eliminan |
| **Simulación de datos** | Generación aleatoria con fallos ocasionales |
| **Manejo de archivos** | Exportación de reporte a `.txt` |
| **Análisis de errores** | Identificación del sensor con más fallos |
| **Agrupación de datos** | Alertas agrupadas por tipo de sensor |
| **Estadísticas** | Promedio, máximo y mínimo por sensor |

---

## Arquitectura del proyecto

```
P1- SIMULADOR DE SENSORES/
│
├── sensor.py       # Clase Sensor  — modela una máquina física y genera lecturas
├── lectura.py      # Clase Lectura — representa un dato capturado
├── monitor.py      # Clase Monitor — sistema central de análisis
└── main.py         # Orquestador  — corre el pipeline completo
```

---

## Lo que está construido

**V1 — Pipeline base**
- [x] Diseño de clases y atributos
- [x] Clase `Sensor` con sus atributos
- [x] Clase `Lectura` con atributo `es_valida`
- [x] Clase `Monitor` con listas de sensores y lecturas
- [x] Método `agregar_sensor()`
- [x] Método `recibir_lectura()` con validación de tipo
- [x] Método `detectar_alertas()`
- [x] Método `generar_reporte()`

**V2 — Simulación realista**
- [x] Generación de datos aleatorios con `random`
- [x] Fallos de sensor simulados — 10% de probabilidad de `"ERROR"`
- [x] Timestamps reales con `datetime`
- [x] Exportación de reporte a archivo `Reporte.txt`

**V3 — Análisis avanzado**
- [x] Identificación del sensor con más errores
- [x] Timestamp de cada alerta en el reporte

**V4 — Análisis detallado** 
- [x] Alertas agrupadas por tipo de sensor
- [x] Estadísticas por sensor — promedio, máximo y mínimo
- [x] Menú interactivo en `main.py`
- [x] Exportar reporte a `.csv`

---

## Output actual

```
El numero total de lecturas es de: 30
Hubo un total de: 4 lecturas invalidas. Esto representa el 13% de todas las lecturas
El sensor con más errores fue el: S02
Hay un total de 14 alertas registradas.

Alertas del tipo: temperatura
- S01 | 2026-08-07 22:56:08 | 197
- S01 | 2026-08-07 22:56:08 | 177

Alertas del tipo: dinero
- S02 | 2026-08-07 22:56:08 | 1975

El estado actual de la fabrica es: normal

Estadisticas por sensor:
S01 | Promedio: 130 | Max: 197 | Min: 44
S02 | Promedio: 952 | Max: 1975 | Min: 402
S03 | Promedio: 179 | Max: 270 | Min: 44
```

---

## Proximo - V5
- [ ] Reestructuración de carpetas — models/, services/, utils/
- [ ] Archivo de configuración centralizado
- [ ] Logging profesional con el módulo logging
- [ ] Persistencia de datos con SQLite
- [ ] Dashboard visual con la librería rich
- [ ] Pruebas unitarias con pytest


---
