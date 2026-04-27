class Monitor:
    """
    Sistema central que maneja la recepción de datos y el análisis.
    """

    def __init__(self):
        self.sensores = [] #Lista de objetos tipo Sensor
        self.lecturas = [] #Lista de objetos tipo Lectura que recibe
        

    def agregar_sensor(self,sensor):
        #Registra un nuevo sensor en el sistema central
        self.sensores.append(sensor)

    def recibir_lectura(self, sensor, valor):
        """
        Punto de entrada para nuevos datos
        Esta será la parte de la validación
        """
        pass