#
# Definir Modelo a partir de la super clase Base Model
from pydantic import BaseModel

# Heredar de la clase Base Model


# Colocar clase Optional para omitir id
from typing import Optional

# Colocar clase Field para colocar valores nulos
from pydantic import Field

class Producto(BaseModel):
    id : Optional[str] = Field(nullable=True)
    nombre : str
    imagen_url : Optional[str] = Field(nullable=True)