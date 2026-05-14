from lectura import Lectura

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
        #Recibe una lectura y la guarda en un objeto para ser validada y almacenada

        nueva_lectura = Lectura(sensor.sensor_id,valor,"2026-01-01")
        
        #La siguiente condicion valida si falla en el tipo de valor necesario para el correcto funcionamiento de la fabrica
        if not(isinstance(valor, (int,float))):
            nueva_lectura.es_valida = False
            
        self.lecturas.append(nueva_lectura)
        
    def detectar_alertas(self):
        #Recorre la lista de lecturas y encuentra cual o cuales  son las peligrosas (es decir las que no son validas)

        alertas = []

        for lectura in self.lecturas:
            if lectura.es_valida:
                for sensor in self.sensores:
                    if sensor.sensor_id == lectura.sensor_id:
                        if lectura.valor > sensor.limite_max:
                            alertas.append(lectura)
        return alertas

    def generar_reporte(self):
        #Reporte visual de los datos obtenidos hasta el momento 

        print(f"El numero total de lecturas es de:{len(self.lecturas)}")
        lecturas_invalidas = len([x for x in self.lecturas if x.es_valida == 0]) #List comprehension para el conteo de las lecturas invalidas
        print(f"Hubo un total de: {lecturas_invalidas}. Esto representa el {round((lecturas_invalidas/len(self.lecturas)*100))}% de todas las lecturas")
        print(f"Hay un total de {len(self.detectar_alertas())} alertas registradas.")
        print(f"El estado actual de la fabrica es: {"normal" if (lecturas_invalidas/len(self.lecturas)*100) < 50 else "en peligro"}")