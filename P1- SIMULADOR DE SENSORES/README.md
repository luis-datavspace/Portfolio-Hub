🏭 Simulador de Pipeline de Datos de Fábrica
Factory Data Pipeline Simulator

Descripción
Proyecto personal que simula un pipeline de datos industrial usando Python orientado a objetos.
El programa simula sensores de una fábrica que envían lecturas de temperatura y presión. Un sistema central (Monitor) recibe esos datos, los valida, detecta anomalías y genera un reporte del estado de la fábrica.
Construido como primer proyecto real fuera de ejercicios básicos, aplicando principios reales de Data Engineering.

Conceptos aplicados

Programación Orientada a Objetos — clases, atributos, métodos, instancias
Validación en la ingesta — detección de datos corruptos antes de procesarlos
Fuente única de verdad — los límites de los sensores viven en un solo lugar
Pipeline de datos por etapas — Ingesta → Filtrado → Reporte
Manejo de datos sucios — lecturas inválidas se marcan y conservan, no se eliminan


🏗️ Arquitectura del proyecto
pipeline_fabrica/
│
├── sensor.py       # Clase Sensor — modela una máquina física
├── lectura.py      # Clase Lectura — representa un dato capturado
├── monitor.py      # Clase Monitor — sistema central de análisis
└── main.py         # Central — corre el pipeline completo

Lo que está hecho

 Diseño de clases y atributos
 Clase Sensor con sus atributos
 Clase Lectura con atributo es_valida
 Clase Monitor con listas de sensores y lecturas
 Método agregar_sensor()
 Método recibir_lectura() con validación de tipo
 Método detectar_alertas()
 Método generar_reporte()
 Pipeline completo corriendo de principio a fin


📊 Output actual
El numero total de lecturas es de: 3
Hubo un total de: 1. Esto representa el 33.33% de todas las lecturas
Hay un total de 1 alertas registradas.
El estado actual de la fabrica es: normal

Versión 2 — Cosas que pienso agregar

 Timestamps reales con el módulo datetime
 Simulación de datos aleatorios con random
 Exportar reporte a archivo .txt