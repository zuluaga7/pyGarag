from tokenize import String
from sqlalchemy import column, Integer, string, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Automoviles(Base):
    __tablename__ = "automoviles"

    id = Column(Integer, primary_key=True, index=True)
    matricula = Column(String(50), unique=True, index=True)
    marca = Column(String(100))
    categoria = Column(String(100))
    año = Column(Integer)


# Creas instancias directamente y accedes a los atributos
nuevo_auto = Automoviles(matricula="ABC123", marca="Toyota", categoria="SUV", año=2022)
print(nuevo_auto.marca)  # Accede directamente al atributo

