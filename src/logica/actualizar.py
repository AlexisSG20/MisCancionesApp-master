from src.modelo.EstudianteBase import Interprete
from src.modelo.estudiante import Album, Medio
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    session = Session()

    estudiante = session.query(Cancion).get(2)
    EstudianteBase = session.query(EstudianteBase).get(4)
    estudiante.nombre = "Pedro Jose"
    cancion.EstudianteBase.append(interprete)
    session.commit()

    session.close()