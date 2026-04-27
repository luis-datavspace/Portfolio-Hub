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
