from monitor import Monitor
from lectura import Lectura
from sensor import Sensor




#TODO ESTO ES UN TIPO DEBUG, NO ES NADA FUNCIONAL PARA EL FINAL PLANEADO, SOLO DE PRUEBA

sistema = Monitor()
sensor_maq_uno = Sensor("S01","temperatura", "°C", 99)
lectura = Lectura("S01", 89, "2026-04-24")
sensor_maq_2 = Sensor("S02", "dinero", "$", 1000)
sensor_maq_3 = Sensor("S03", "bodycount", "personas" , 2)


print(sensor_maq_uno.sensor_id)
print(lectura.valor)


sistema.agregar_sensor(sensor_maq_uno)
sistema.agregar_sensor(sensor_maq_2)
sistema.agregar_sensor(sensor_maq_3)
print(len(sistema.sensores))

sistema.recibir_lectura(sensor_maq_uno, 85)
sistema.recibir_lectura(sensor_maq_uno, 150)
sistema.recibir_lectura(sensor_maq_uno, 'Error')
print(len(sistema.lecturas))

alertas = sistema.detectar_alertas()
print(len(alertas))

sistema.generar_reporte()