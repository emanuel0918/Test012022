#
# Definir Modelo a partir de la super clase Base Model
from pydantic import BaseModel

# Heredar de la clase Base Model


# Colocar clase Optional para omitir id
from typing import Optional

# Colocar clase Field para colocar valores nulos
from pydantic import Field

class Usuario(BaseModel):
    # El id se genera derivable del servidor en MongoDB
    id : Optional[str] = Field(nullable=True)
    uuid : Optional[str]
    nombre : str
    apellido_paterno : str
    apellido_materno : Optional[str] = Field(nullable=True)
    correo : str
    usuario : str
    password : str
    # La fecha se genera de manera automatica
    fecha_creacion : Optional[str] = Field(nullable=True)
    # La fecha se genera de manera automatica
    fecha_modificacion : Optional[str] = Field(nullable=True)
    admin_creador : Optional[str] = Field(nullable=True)