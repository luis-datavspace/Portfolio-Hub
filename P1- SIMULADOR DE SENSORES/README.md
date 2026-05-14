# 🏭 Simulador de Pipeline de Datos de Fábrica

---

##  Descripción

Proyecto personal que simula un **pipeline de datos industrial** usando Python orientado a objetos.

El programa simula sensores de una fábrica que envían lecturas de temperatura y presión. Un sistema central (Monitor) recibe esos datos, los valida, detecta anomalías y genera un reporte del estado de la fábrica.

Construido como **primer proyecto real** fuera de ejercicios básicos o problemas de cursos educativos, esto aplicando principios reales de Data Engineering.

---

## 🧠 Conceptos aplicados

| Concepto | Descripción |
|---|---|
| **POO** | Clases, atributos, métodos, instancias |
| **Validación en la ingesta** | Detección de datos corruptos antes de procesarlos |
| **Fuente única de verdad** | Los límites de los sensores viven en un solo lugar |
| **Pipeline por etapas** | Ingesta → Filtrado → Reporte |
| **Manejo de datos sucios** | Lecturas inválidas se marcan y conservan, no se eliminan |

---

## 🏗️ Arquitectura del proyecto

```
P1- SIMULADOR DE SENSORES/
│
├── models/
│   ├── sensor.py       # Clase Sensor  — modela una máquina física
│   ├── lectura.py      # Clase Lectura — representa un dato capturado
│   └── monitor.py      # Clase Monitor — sistema central de análisis
│
└── main.py             # Central — orquestador del pipeline completo
```

---

## ✅ Lo que está construido

- [x] Diseño de clases y atributos
- [x] Clase `Sensor` con sus atributos
- [x] Clase `Lectura` con atributo `es_valida`
- [x] Clase `Monitor` con listas de sensores y lecturas
- [x] Método `agregar_sensor()`
- [x] Método `recibir_lectura()` con validación de tipo
- [x] Método `detectar_alertas()`
- [x] Método `generar_reporte()`
- [x] Pipeline completo corriendo de principio a fin

---

## 📊 Output actual

```
El numero total de lecturas es de: 3
Hubo un total de: 1. Esto representa el 33.33% de todas las lecturas
Hay un total de 1 alertas registradas.
El estado actual de la fabrica es: normal
```

---

## 🔜 Versión 2 — Próximamente

- [ ] Timestamps reales con el módulo `datetime`
- [ ] Simulación de datos aleatorios con `random`
- [ ] Exportar reporte a archivo `.txt`

---
