from src.modelo.cancion import Cancion
from src.modelo.EstudianteBase import Interprete
from src.modelo.estudiante import Album, Medio
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    session = Session()

    cancion2 = session.query(Cancion).get(2)
    session.delete(cancion2)

    session.commit()
    session.close()