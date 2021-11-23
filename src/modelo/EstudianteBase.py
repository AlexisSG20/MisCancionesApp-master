from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base

class EstudianteBase(Base):
    __tablename__ = 'EstudianteBase'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellidos = Column(String)
    RegistroNotas = Column(String)
