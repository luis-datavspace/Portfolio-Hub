class Lectura:
    
    """
    Representa un punto de dato individual generado por un sensor.
    """

    def __init__(self, sensor_id, valor, timestamp):
        self.sensor_id = sensor_id
        self.valor = valor
        self.timestamp = timestamp
        #Validación por defecto; la logica de validación cambia a False si el dato es basura.
        self.es_valida = True
