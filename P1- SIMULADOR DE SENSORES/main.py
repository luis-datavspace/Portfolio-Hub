from monitor import Monitor
from lectura import Lectura
from sensor import Sensor

# Orquestador principal del pipeline

# Registra sensores, genera lecturas aleatorias y corre el reporte

sistema = Monitor()
sensor_maq_uno = Sensor("S01","temperatura", "°C", 99)
sensor_maq_2 = Sensor("S02", "dinero", "$", 1000)
sensor_maq_3 = Sensor("S03", "bodycount", "personas" , 150)

sistema.agregar_sensor(sensor_maq_uno)
sistema.agregar_sensor(sensor_maq_2)
sistema.agregar_sensor(sensor_maq_3)

# cada sensor genera 10 lecturas aleatorias

for lectura in range(10):
    for sensor in sistema.sensores:
        sistema.recibir_lectura(sensor, sensor.generar_lectura())
        
#Se generan los datos a explorar antes del menu interactivo.



# Procedo a realizar el menu interactivo para el proyecto, para mas orden y legibilidad.


while True:

    print("===================================")
    print("       SISTEMA DE MONITOREO        ")
    print("===================================")
    print("1. Ver reporte general")
    print("2. Ver estadísticas por sensor")
    print("3. Exportar reporte a CSV")
    print("4. Salir")
    print("===================================")

    decision = (input("¿Qué deseas hacer? ")).upper()

    if decision in ("1","UNO", "VER REPORTE GENERAL"):
        print("")
        sistema.generar_reporte()
        input("\nPresione Enter para continuar..... ")

    elif decision in ("2","DOS","VER ESTADISTICAS POR SENSOR"):
        print("")
        sistema.estadisticas_por_sensor()
        input("\nPresione Enter para continuar..... ")

    elif decision in ("3","EXPORTAR REPORTE A CSV","TRES"):
                print("")
                sistema.exportar_csv()
                input("\nPresione Enter para continuar..... ")

    elif decision in ("4","SALIR","CUATRO"):
        print("Saliendo.......")
        
    else:
        print("\nOpción invalida. Intentalo de nuevo.\n")
