🏭 Simulador de Pipeline de Datos de Fábrica
Factory Data Pipeline Simulator
 - Descripción

Proyecto personal que simula un pipeline de datos industrial usando Python orientado a objetos.

El programa simula sensores de una fábrica que envían lecturas de temperatura y presión. Un sistema central (Monitor) recibe esos datos, los valida, detecta anomalías y genera un reporte del estado de la fábrica — tanto en consola como en archivo .txt.

Construido como primer proyecto real fuera de ejercicios básicos, aplicando principios reales de Data Engineering.

- Conceptos aplicados -
Concepto	Descripción
POO	Clases, atributos, métodos, instancias
Validación en la ingesta	Detección de datos corruptos antes de procesarlos
Fuente única de verdad	Los límites de los sensores viven en un solo lugar
Pipeline por etapas	Ingesta → Filtrado → Reporte
Manejo de datos sucios	Lecturas inválidas se marcan y conservan, no se eliminan
Simulación de datos	Generación aleatoria con fallos ocasionales
Manejo de archivos	Exportación de reporte a .txt

- Arquitectura del proyecto -
P1- SIMULADOR DE SENSORES/
│
├── sensor.py       # Clase Sensor  — modela una máquina física y genera lecturas
├── lectura.py      # Clase Lectura — representa un dato capturado
├── monitor.py      # Clase Monitor — sistema central de análisis
└── main.py         # Orquestador  — corre el pipeline completo
✅ Lo que está construido

V1 — Pipeline base

 Diseño de clases y atributos
 Clase Sensor con sus atributos
 Clase Lectura con atributo es_valida
 Clase Monitor con listas de sensores y lecturas
 Método agregar_sensor()
 Método recibir_lectura() con validación de tipo
 Método detectar_alertas()
 Método generar_reporte()

V2 — Simulación realista

 Generación de datos aleatorios con random
 Fallos de sensor simulados — 10% de probabilidad de "ERROR"
 Timestamps reales con datetime
 Exportación de reporte a archivo Reporte.txt

- Output actual - 

Consola:

El numero total de lecturas es de: 30
Hubo un total de: 3. Esto representa el 10% de todas las lecturas
Hay un total de 13 alertas registradas.
El estado actual de la fabrica es: normal

Reporte.txt — se genera automáticamente en cada corrida con el mismo contenido.

 - Ideas para V3 - 
 Identificar qué sensor generó más errores
 Mostrar el timestamp de cada alerta en el reporte
 Agregar más tipos de sensores con distintos rangos

