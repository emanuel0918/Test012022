#
# Crear Modulo para Definir los End Points del Producto
from fastapi import APIRouter
# Importar la clase de Response para poder
# Resultar una Respuesta con formato
from fastapi import Response, status
# Importar Modelo
from models.producto import Producto
# Patron de Disenio DAO
from dao.producto import get_all_productos, insert_producto, get_producto_by_id, delete_producto, update_producto

# Importar tipo de dato List
from typing import List

# Importar un Codigo de Status para Borrar
from starlette.status import HTTP_204_NO_CONTENT

# 
producto = APIRouter()

# Traer todos los productos
@producto.get('/producto', response_model=List[Producto], tags=["Producto"])
def obtener_productos() :
    return get_all_productos()

# Insertar producto
@producto.post('/producto', response_model=Producto, tags=["Producto"])
def crear_producto(producto : Producto) :
    return insert_producto(producto)

# Traer un producto
@producto.get('/producto/{id}', response_model=Producto, tags=["Producto"])
def obtener_producto(id : str) :
    return get_producto_by_id(id)


# Actualizar un producto
@producto.put('/producto/{id}', response_model=Producto, tags=["Producto"])
def actualizar_producto(id : str, producto : dict) :
    return update_producto(id, producto)

# Eliminar un producto
@producto.delete('/producto/{id}', status_code=HTTP_204_NO_CONTENT, tags=["Producto"])
def borrar_producto(id : str) :
    delete_producto(id)
    return Response(status_code=HTTP_204_NO_CONTENT)
