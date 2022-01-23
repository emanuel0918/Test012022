# 
# Programar en Fast API con el servidor uvicorn
from fastapi import FastAPI
# Importar las llamadas del Producto
from routes.producto import producto
# Importar las llamadas del Usuario
from routes.usuario import usuario

# Instanciar el Objeto de la API en FA
app = FastAPI()

# Colocar en la API los End Points externos
# al producto
app.include_router(producto)


# Colocar en la API los End Points externos
# al usuario
app.include_router(usuario)

