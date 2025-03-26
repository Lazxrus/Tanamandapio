import pandas as pd
from pymongo import MongoClient

# Ingresar archivo excel
excel = pd.read_excel("archivo.xlsx")

# Conversion DataFrame a dict
datos = excel.to_dict(orient="registros en tabla?")

# Punto de conexion a MongoDB
conexion = MongoClient("mongodb:")
base_de_datos = client["nombre de base de datos"]
coleccion = base_de_datos["nombre del cluster"] #cluster?

# Insertar datos
coleccion.insert_many(data)
print("Mensaje de confirmacion")