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


class Moto(Base):
    __tablename__ = "motos"

    id = Column(Integer, primary_key=True, index=True)
    matricula = Column(String(50), unique=True, index=True, nullable=False)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    año = Column(Integer, nullable=False)
    cilindraje = Column(Integer, nullable=False)


class Barco(Base):
    __tablename__ = 'barcos'

    id = Column(Integer, primary_key=True, index=True)
    matricula = Column(String(100), unique=True, index=True)
    marca = Column(String(100))
    modelo = Column(String(100))
    año = Column(Integer)
    capacidad = Column(Integer)

