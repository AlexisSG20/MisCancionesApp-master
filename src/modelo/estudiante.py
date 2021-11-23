import enum

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Medio(enum.Enum):
    Seleccionar = 1
    Editar = 2
    Agregar = 3


class Album(Base):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True)
    Apellidos = Column(String)
    Nombres = Column(String)
    edad = Column(Integer)
    medio = Column(Enum(Medio))

