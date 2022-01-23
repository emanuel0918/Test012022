# Importar Modelo
from models.producto import Producto
# Importar conexion a la BD
from config.db import collection_producto
# Importar el tipo de dato ObjectId
from bson import ObjectId


# Insertar un Producto
def insert_producto (producto : Producto):
    # Castear JSON a tipo de dato Dict
    nuevo_producto = dict(producto)
    # Omitir valor por defecto id
    # Valor id "_id"
    del nuevo_producto["id"]

    # Insertar
    id = collection_producto.insert_one(nuevo_producto).inserted_id
    # Recuperar el id

    # Imprimir objeto creado
    return get_producto_by_id(id)


# Obtener un Producto
def get_producto (producto) -> dict:
    return {
        "id" : str(producto["_id"]),
        "nombre" : producto["nombre"],
        "imagen_url" : producto["imagen_url"]

    }

# Obtener un Producto por Id
def get_producto_by_id (id) :
    # Castear el tipo de dato en la consulta 
    # correspondiente al tipo de dato de ID
    # en MongoDB
    u = collection_producto.find_one({"_id" : ObjectId(id)})
    return get_producto(u)

# Obtener todos los Productos
def get_all_productos() -> list:
    # Lanzar consulta general
    productos = collection_producto.find()
    # Obtener todos los productos
    return [get_producto(producto) for producto in productos]

# Borrar Producto
def delete_producto(id : str):
    collection_producto.find_one_and_delete({"_id" : ObjectId(id)})

# Actualizar Producto
def update_producto(id : str, producto : dict):
    # Leer diccionario desde el end point con llaves opcionales
    nuevo_producto = dict(producto)
    # Hacer un backup del producto anterior
    producto_anterior = get_producto_by_id(id)
    # Checar si la llave nombre existe
    if "nombre" in nuevo_producto:
        # Si el nombre nuevo es diferente no copiarlo
        if nuevo_producto["nombre"] != producto_anterior["nombre"]:
            # Si el nombre nuevo es nulo no se remplaza
            if len(nuevo_producto["nombre"]) == 0 :
                # Reestablecer valor del nombre del producto anterior
                nuevo_producto["nombre"] = producto_anterior["nombre"]
    collection_producto.find_one_and_update({"_id" : ObjectId(id)}, {"$set" : nuevo_producto})
    return get_producto_by_id(id)