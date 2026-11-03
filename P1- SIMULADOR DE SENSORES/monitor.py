from lectura import Lectura
from datetime import datetime
import csv

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
        #Recorre la lista de lecturas y encuentra cual o cuales  son las peligrosas (Las peligrosas son las válidas que pasan el límite, y las no válidas son basura del sensor)

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

        #El contenido lo reconstrui una sola vez como lista de líneas,
        #y esa misma lista se imprime en consola y se guarda en Reporte.txt.
        

        # Sin lecturas no hay nada que reportar (evita dividir entre cero)
        if not self.lecturas:
            print("No hay lecturas registradas. No se puede generar el reporte.")
            return

        alertas = self.detectar_alertas()
        lecturas_invalidas = len([x for x in self.lecturas if not x.es_valida])
        porcentaje_invalidas = round(lecturas_invalidas / len(self.lecturas) * 100)
        estado = self.calcular_estado()

        lineas = []
        lineas.append(f"El numero total de lecturas es de: {len(self.lecturas)}")
        lineas.append(f"Hubo un total de: {lecturas_invalidas} lecturas invalidas. Esto representa el {porcentaje_invalidas}% de todas las lecturas")
        lineas.append(f"El sensor con más errores fue el: {self.sensor_con_mas_errores()}")
        lineas.append(f"Hay un total de {len(alertas)} alertas registradas.")

        alertas_por_tipo = {}
        for alerta in alertas:
            if alerta.tipo not in alertas_por_tipo:
                alertas_por_tipo[alerta.tipo] = [alerta]
            else:
                alertas_por_tipo[alerta.tipo].append(alerta)

        for tipo, lista_alertas in alertas_por_tipo.items():
            lineas.append(f"\nAlertas del tipo: {tipo}")
            for alerta in lista_alertas:
                lineas.append(f"- {alerta.sensor_id} | {alerta.timestamp} | {alerta.valor}")

        lineas.append(f"\nEl estado actual de la fabrica es: {estado}")

        # La misma lista sirve para los dos destinos
        for linea in lineas:
            print(linea)

        with open("Reporte.txt", "w") as archivo:
            for linea in lineas:
                archivo.write(linea + "\n")

    def sensor_con_mas_errores(self):
        conteo = {}

        for lectura in self.lecturas:
            if not(lectura.es_valida): # Solo analiza lecturas inválidas (es_valida == False)
                if lectura.sensor_id in conteo:
                    conteo[lectura.sensor_id] += 1
                else:
                    conteo[lectura.sensor_id] = 1
        if not conteo:
            return "Ninguno (sin errores)" #Evita error por elemento vacio 

        sensor_mas_erratico = max(conteo, key=conteo.get)

        return sensor_mas_erratico

    def calcular_estado(self):

        # Calcula el estado general de la fábrica y lo devuelve como texto. De una manera mejor planteada, me estaba enfocando en lecturas invalidad (basura) que en el real peligro 
        # Que son las que superan el limite
        #No imprime nada: solo calcula, y generar_reporte() lo muestra para no tener que estar calculando cada vez que quiera saber el estado.


        validas = [l for l in self.lecturas if l.es_valida]

        if not validas:
            return "sin datos"

        alertas = self.detectar_alertas()
        pct_alertas = len(alertas) / len(validas) * 100
        pct_invalidas = (len(self.lecturas) - len(validas)) / len(self.lecturas) * 100

        if pct_alertas > 60:
            return "peligro"
        elif pct_alertas >= 25 or pct_invalidas >= 20:
            return "atención"
        else:
            return "normal"    


    def calcular_estadisticas(self):
        #Evita duplicar codigo inecesario teniendo solo que hacer llamado de la funcion, pase de largo antes de esto.

        sensores = {}
        stats = {}

        for sensor in self.sensores:
            if sensor.sensor_id not in sensores:
                sensores[sensor.sensor_id] = []

            for lectura in self.lecturas:
                if sensor.sensor_id == lectura.sensor_id and lectura.es_valida:
                    sensores[sensor.sensor_id].append(lectura.valor)


        for id_sensor, lista_de_valores in sensores.items():
            if lista_de_valores:
                stats[id_sensor] = {"Promedio": round((sum(lista_de_valores))/len(lista_de_valores)), "Max": max(lista_de_valores), "Min":min(lista_de_valores)}
            else:
                stats[id_sensor] = {"Promedio": 'Sin Datos' , "Max": 'Sin Datos' , "Min":'Sin Datos'}


        return stats 
            

    def estadisticas_por_sensor(self):

        e_p_s = self.calcular_estadisticas()

        print("Estadisticas por sensor:\n")

        for id_sensor, datos in e_p_s.items():
            print(f"ID Sensor: {id_sensor} | Promedio: {datos['Promedio']} | Max: {datos['Max']} | Min: {datos['Min']}")


    def exportar_csv(self):

        estadisticas = self.calcular_estadisticas()

        with open("Reporte.csv", "w", newline="") as archvio_csv:
            writer = csv.writer(archvio_csv)
            writer.writerow([])
            writer.writerow(["LECTURAS"])
            writer.writerow(["ID Sensor","Tipo","Valor","Fecha y Hora","Validez"])

            for lectura in self.lecturas:
                writer.writerow([lectura.sensor_id,lectura.tipo,lectura.valor,lectura.timestamp,lectura.es_valida])

            writer.writerow([])
            writer.writerow(["ALERTAS"])
            writer.writerow(["ID Sensor","Tipo","Valor","Fecha y Hora"])

            for alerta in self.detectar_alertas():
                writer.writerow([alerta.sensor_id,alerta.tipo,alerta.valor,alerta.timestamp])

            writer.writerow([])
            writer.writerow(["ESTADISTICAS"])
            writer.writerow(["ID Sensor","Promedio","Max","Min"])
            for id_sensor, datos in estadisticas.items():
                writer.writerow([id_sensor, datos["Promedio"], datos["Max"], datos["Min"]])




            

