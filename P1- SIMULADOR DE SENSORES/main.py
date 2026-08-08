from monitor import Monitor
from lectura import Lectura
from sensor import Sensor

# Orquestador principal del pipeline
#I AM BACK!

#TODO ESTO ES UN TIPO DEBUG, NO ES NADA FUNCIONAL PARA EL FINAL PLANEADO, SOLO DE PRUEBA

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
        



alertas = sistema.detectar_alertas()
print(len(alertas))

sistema.generar_reporte()
sistema.estadisticas_por_sensor()