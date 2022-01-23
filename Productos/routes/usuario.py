#
# Crear Modulo para Definir los End Points del Usuario
from fastapi import APIRouter
# Importar la clase de Response para poder
# Resultar una Respuesta con formato
from fastapi import Response, status
# Importar Modelo
from models.usuario import Usuario
# Patron de Disenio DAO
from dao.usuario import get_all_usuarios, insert_usuario, get_usuario_by_id, delete_usuario, update_usuario

# Importar tipo de dato List
from typing import List

# Importar un Codigo de Status para Borrar
from starlette.status import HTTP_204_NO_CONTENT

# 
usuario = APIRouter()

# Traer todos los usuarios
@usuario.get('/usuario', response_model=List[Usuario], tags=["Usuario"])
def obtener_usuarios() :
    return get_all_usuarios()

# Insertar usuario
@usuario.post('/usuario', response_model=Usuario, tags=["Usuario"])
def crear_usuario(usuario : Usuario) :
    return insert_usuario(usuario)

# Traer un usuario
@usuario.get('/usuario/{id}', response_model=Usuario, tags=["Usuario"])
def obtener_usuario(id : str) :
    return get_usuario_by_id(id)


# Actualizar un usuario
@usuario.put('/usuario/{id}', response_model=Usuario, tags=["Usuario"])
def actualizar_usuario(id : str, usuario : dict) :
    return update_usuario(id, usuario)

# Eliminar un usuario
@usuario.delete('/usuario/{id}', status_code=HTTP_204_NO_CONTENT, tags=["Usuario"])
def borrar_usuario(id : str) :
    delete_usuario(id)
    return Response(status_code=HTTP_204_NO_CONTENT)
