from lectura import Lectura
from datetime import datetime

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

    def recibir_lectura(self, sensor, valor,):
        #Recibe una lectura y la guarda en un objeto para ser validada y almacenada

        nueva_lectura = Lectura(sensor.sensor_id,valor, datetime.now(), sensor.tipo)
        
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

    def generar_reporte(self) -> None:
        #Reporte visual de los datos obtenidos hasta el momento 

        alertas = self.detectar_alertas()
        print(f"El numero total de lecturas es de:{len(self.lecturas)}")
        lecturas_invalidas = len([x for x in self.lecturas if x.es_valida == 0]) #List comprehension para el conteo de las lecturas invalidas
        print(f"Hubo un total de: {lecturas_invalidas} lecturas invalidas. Esto representa el {round((lecturas_invalidas/len(self.lecturas)*100))}% de todas las lecturas")
        print(f"El sensor con más errores fue el: {self.sensor_con_mas_errores()}")
        print(f"Hay un total de {len(alertas)} alertas registradas.")

        alertas_por_tipo = {}
        for alerta in alertas:
            if alerta.tipo not in alertas_por_tipo:
                alertas_por_tipo[alerta.tipo] = [alerta]
            else:
                alertas_por_tipo[alerta.tipo].append(alerta)

        for tipo, lista_alertas in alertas_por_tipo.items():
            print(f"\nAlertas del tipo: {tipo}\n")
            for alerta in lista_alertas:
                print(f"- {alerta.sensor_id} | {alerta.timestamp} | {alerta.valor}")


        print(f"El estado actual de la fabrica es: {"normal" if (lecturas_invalidas/len(self.lecturas)*100) < 50 else "en peligro"}")

        with open("Reporte.txt", "w") as archivo:

            archivo.write(f"El numero total de lecturas es de:{len(self.lecturas)} \n")
            archivo.write(f"Hubo un total de: {lecturas_invalidas}. Esto representa el {round((lecturas_invalidas/len(self.lecturas)*100))}% de todas las lecturas\n")
            archivo.write(f"El sensor con más errores fue el: {self.sensor_con_mas_errores()}")

            archivo.write(f"Hay un total de {len(alertas)} alertas registradas.\n")

            for tipo, lista_alertas in alertas_por_tipo.items():
                        archivo.write(f"Alertas del tipo: {tipo}\n")
                        for alerta in lista_alertas:
                            archivo.write(f"- {alerta.sensor_id} | {alerta.timestamp} | {alerta.valor}")

    def sensor_con_mas_errores(self):
        conteo = {}

        for lectura in self.lecturas:
            if not(lectura.es_valida): # Solo analiza lecturas inválidas (es_valida == False)
                if lectura.sensor_id in conteo:
                    conteo[lectura.sensor_id] += 1
                else:
                    conteo[lectura.sensor_id] = 1

        sensor_mas_erratico = max(conteo, key=conteo.get)

        return sensor_mas_erratico

    def estadisticas_por_sensor(self):

        print("Estadisticas por sensor: ")

        sensores = {}

        for sensor in self.sensores:
            if sensor.sensor_id not in sensores:
                sensores[sensor.sensor_id] = []

            for lectura in self.lecturas:
                if sensor.sensor_id == lectura.sensor_id and lectura.es_valida:
                    sensores[sensor.sensor_id].append(lectura.valor)

        for id_sensor,valor in sensores.items():
            print(f"{id_sensor} | Promedio: {round((sum(valor))/len(valor))} | Max: {max(valor)} | Min: {min(valor)} ")


