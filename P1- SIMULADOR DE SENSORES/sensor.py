import random

class Sensor:
    
    """
    Representa un sensor físico en la fábrica.
    Se encarga de identificar qué se mide y cuáles son sus límites.
    """
    
    def __init__(self, sensor_id, tipo, unidad, limite_max):
        self.sensor_id = sensor_id #ID
        self.tipo = tipo #Qué mide 
        self.unidad = unidad #unidad de medida
        self.limite_max = limite_max #limite maximo antes de error

    # Simula una lectura del sensor.
    def generar_lectura(self):

        #Gracias a que la función random.random)= genera un numero entre 0.0 y 1.0, sacamos la probabilidad de fallo
        if random.random() < 0.1:
            return "ERROR" #10% de probabilidad de fallo (devuelve "ERROR")
        
        else:
            return random.randint(20,(self.limite_max*2)) # En caso normal devuelve un entero aleatorio entre 20 y el doble del límite máximo