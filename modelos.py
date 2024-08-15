from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Automovil(Base):
    __tablename__ = "automoviles"

    id = Column(Integer, primary_key=True, index=True)
    matricula = Column(String(50), unique=True, index=True)
    marca = Column(String(100))
    categoria = Column(String(100))
    año = Column(Integer)

class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    matricula = Column(String(50), unique=True, index=True)
    marca = Column(String(100))
    categoria = Column(String(100))
    año = Column(Integer)