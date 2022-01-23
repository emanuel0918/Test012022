# Importar Modelo
from models.usuario import Usuario
# Importar conexion a la BD
from config.db import collection_usuario
# Importar el tipo de dato ObjectId
from bson import ObjectId
# Importar el tipo de dato uuid
import uuid
# Importar biblioteca para poder encryptar texto
from passlib.hash import sha256_crypt
# Importar biblioteca para usar fechas
from datetime import datetime



# Insertar un Usuario
def insert_usuario (usuario : Usuario):
    # Castear JSON a tipo de dato Dict
    nuevo_usuario = dict(usuario)
    # Cifrar Contrasenia con Algoritmo SHA 256
    nuevo_usuario["password"] = sha256_crypt.encrypt(nuevo_usuario["password"])
    # Omitir valor por defecto id
    # Valor id "_id"
    del nuevo_usuario["id"]
    # Asignar el valor de la fecha de creacion
    # Asignar el valor de la fecha de modificacion
    nuevo_usuario["fecha_creacion"] = str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    nuevo_usuario["fecha_modificacion"] = str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    # Generar el uuid
    nuevo_usuario["uuid"] = str(uuid.uuid4())

    # Insertar
    id = collection_usuario.insert_one(nuevo_usuario).inserted_id
    # Recuperar el id

    # Imprimir objeto creado
    return get_usuario_by_id(id)


# Obtener un Usuario
def get_usuario (usuario) -> dict:
    return {
        "id" : str(usuario["_id"]),
        "uuid" : usuario["uuid"],
        "nombre" : usuario["nombre"],
        "apellido_paterno" : usuario["apellido_paterno"],
        "apellido_materno" : usuario["apellido_materno"],
        "correo" : usuario["correo"],
        "usuario" : usuario["usuario"],
        "password" : usuario["password"],
        "fecha_creacion" : usuario["fecha_creacion"],
        "fecha_modificacion" : usuario["fecha_modificacion"],
        "admin_creador" : usuario["admin_creador"]

    }

# Obtener un Usuario por Id
def get_usuario_by_id (id) :
    # Castear el tipo de dato en la consulta 
    # correspondiente al tipo de dato de ID
    # en MongoDB
    u = collection_usuario.find_one({"_id" : ObjectId(id)})
    return get_usuario(u)

# Obtener todos los Usuarios
def get_all_usuarios() -> list:
    # Lanzar consulta general
    usuarios = collection_usuario.find()
    # Obtener todos los usuarios
    return [get_usuario(usuario) for usuario in usuarios]

# Borrar Usuario
def delete_usuario(id : str):
    collection_usuario.find_one_and_delete({"_id" : ObjectId(id)})

# Actualizar Usuario
def update_usuario(id : str, usuario : dict):
    # Leer diccionario desde el end point con llaves opcionales
    nuevo_usuario = dict(usuario)
    # Hacer un backup del usuario anterior
    usuario_anterior = get_usuario_by_id(id)
    # Checar si la llave nombre existe
    if "nombre" in nuevo_usuario:
        # Si el nombre nuevo es diferente no copiarlo
        if nuevo_usuario["nombre"] != usuario_anterior["nombre"]:
            # Si el nombre nuevo es nulo no se remplaza
            if len(nuevo_usuario["nombre"]) == 0 :
                # Reestablecer valor del nombre del usuario anterior
                nuevo_usuario["nombre"] = usuario_anterior["nombre"]
    # Checar si la llave apellido paterno existe
    if "apellido_paterno" in nuevo_usuario:
        # Si el apellido paterno nuevo es diferente no copiarlo
        if nuevo_usuario["apellido_paterno"] != usuario_anterior["apellido_paterno"]:
            # Si el apellido paterno nuevo es nulo no se remplaza
            if len(nuevo_usuario["apellido_paterno"]) == 0 :
                # Reestablecer valor del apellido paterno del usuario anterior
                nuevo_usuario["apellido_paterno"] = usuario_anterior["apellido_paterno"]
    # Checar si la llave apellido materno existe
    if "apellido_materno" in nuevo_usuario:
        # Si el apellido materno nuevo es diferente no copiarlo
        if nuevo_usuario["apellido_materno"] != usuario_anterior["apellido_materno"]:
            # Si el apellido materno nuevo es nulo no se remplaza
            if len(nuevo_usuario["apellido_materno"]) == 0 :
                # Reestablecer valor del apellido materno del usuario anterior
                nuevo_usuario["apellido_materno"] = usuario_anterior["apellido_materno"]
    # Checar si la llave correo existe
    if "correo" in nuevo_usuario:
        # Si el correo nuevo es diferente no copiarlo
        if nuevo_usuario["correo"] != usuario_anterior["correo"]:
            # Si el correo nuevo es nulo no se remplaza
            if len(nuevo_usuario["correo"]) == 0 :
                # Reestablecer valor del correo del usuario anterior
                nuevo_usuario["correo"] = usuario_anterior["correo"]
    # Checar si la llave usuario existe
    if "usuario" in nuevo_usuario:
        # Si el usuario nuevo es diferente no copiarlo
        if nuevo_usuario["usuario"] != usuario_anterior["usuario"]:
            # Si el usuario nuevo es nulo no se remplaza
            if len(nuevo_usuario["usuario"]) == 0 :
                # Reestablecer valor del usuario del usuario anterior
                nuevo_usuario["usuario"] = usuario_anterior["usuario"]
    # Checar si la llave password existe
    if "password" in nuevo_usuario:
        # Si el password nuevo no es nulo se remplaza
        if len(nuevo_usuario["password"]) != 0 :
            nuevo_usuario["password"] = sha256_crypt.encrypt(nuevo_usuario["password"])
    # Asignar el valor de la fecha de modificacion
    nuevo_usuario["fecha_modificacion"] = str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    collection_usuario.find_one_and_update({"_id" : ObjectId(id)}, {"$set" : nuevo_usuario})
    return get_usuario_by_id(id)