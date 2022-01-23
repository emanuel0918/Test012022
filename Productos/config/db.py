#
# Importar de la biblioteca disponible de pymongo
# el cliente para conectarse al servidor en
# Mongo DB Atlas
from pymongo import MongoClient

# Definir el cliente
myclient = MongoClient("mongodb+srv://alumno:alumno@cluster010621.j9b4t.mongodb.net/")

# Definir la DB
mydb = myclient["Productos"]

# Collection Usuarios
collection_usuario = mydb["Usuarios"]

# Collection Productos
collection_producto = mydb["Productos"]
