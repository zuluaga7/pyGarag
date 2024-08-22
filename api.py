from typing import List
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware
from base_de_datos import SessionLocal, engine
from modelos import Base, Automovil, Moto, Barco

app = FastAPI()
app.title = "Garage la z"

# Configurar el middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes, puedes especificar una lista de orígenes permitidos si lo prefieres
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"])  # Permitir todos los encabezados

# Crear las tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic models para Automóvil
class AutomovilCreate(BaseModel):
    matricula: str
    marca: str
    categoria: str
    año: int


class AutomovilResponse(BaseModel):
    id: int
    matricula: str
    marca: str
    categoria: str
    año: int

    class Config:
        orm_mode = True


# Endpoints de automóviles
@app.post("/automoviles", tags=["Automóviles"], response_model=AutomovilResponse)
def crear_automovil(automovil: AutomovilCreate, db: Session = Depends(get_db)):
    db_automovil = Automovil(**automovil.dict())
    db.add(db_automovil)
    db.commit()
    db.refresh(db_automovil)
    return db_automovil


@app.get("/automoviles/", tags=["Automóviles"], response_model=List[AutomovilResponse])
def obtener_automoviles(db: Session = Depends(get_db)):
    inventario = db.query(Automovil).all()
    return inventario


@app.get("/automoviles/{matricula}", tags=["Automóviles"], response_model=AutomovilResponse)
def obtener_automovil(matricula: str, db: Session = Depends(get_db)):
    db_automovil = db.query(Automovil).filter(Automovil.matricula == matricula).first()
    if db_automovil is None:
        raise HTTPException(status_code=404, detail="Automóvil no encontrado")
    return db_automovil


@app.put("/automoviles/{matricula}", tags=["Automóviles"], response_model=AutomovilResponse)
def actualizar_automovil(matricula: str, automovil: AutomovilCreate, db: Session = Depends(get_db)):
    db_automovil = db.query(Automovil).filter(Automovil.matricula == matricula).first()
    if db_automovil is None:
        raise HTTPException(status_code=404, detail="Automóvil no encontrado")
    for key, value in automovil.dict().items():
        setattr(db_automovil, key, value)
    db.commit()
    db.refresh(db_automovil)
    return db_automovil


@app.delete("/automoviles/{matricula}", tags=["Automóviles"], response_model=AutomovilResponse)
def eliminar_automovil(matricula: str, db: Session = Depends(get_db)):
    db_automovil = db.query(Automovil).filter(Automovil.matricula == matricula).first()
    if db_automovil is None:
        raise HTTPException(status_code=404, detail="Automóvil no encontrado")
    db.delete(db_automovil)
    db.commit()
    return db_automovil

@app.delete("/automoviles/", tags=["Automóviles"], status_code=204)
def eliminar_todo_inventario_automoviles(db: Session = Depends(get_db)):
    db.query(Automovil).delete()
    db.commit()
    return {"detail": "Todo el inventario de automóviles ha sido eliminado"}


# Pydantic models para Moto
class MotoCreate(BaseModel):
    matricula: str
    marca: str
    modelo: str
    año: int
    cilindraje: int


class MotoResponse(MotoCreate):
    id: int

    class Config:
        orm_mode = True


# Endpoints de motos
@app.post("/motos/", tags=["Motos"], response_model=MotoResponse)
def crear_moto(moto: MotoCreate, db: Session = Depends(get_db)):
    db_moto = Moto(**moto.dict())
    db.add(db_moto)
    db.commit()
    db.refresh(db_moto)
    return db_moto


@app.get("/motos/", tags=["Motos"], response_model=List[MotoResponse])
def obtener_motos(db: Session = Depends(get_db)):
    return db.query(Moto).all()


@app.get("/motos/{matricula}", tags=["Motos"], response_model=MotoResponse)
def obtener_moto(matricula: str, db: Session = Depends(get_db)):
    moto = db.query(Moto).filter(Moto.matricula == matricula).first()
    if moto is None:
        raise HTTPException(status_code=404, detail="Moto no encontrada")
    return moto


@app.put("/motos/{matricula}", tags=["Motos"], response_model=MotoResponse)
def actualizar_moto(matricula: str, moto: MotoCreate, db: Session = Depends(get_db)):
    db_moto = db.query(Moto).filter(Moto.matricula == matricula).first()
    if db_moto is None:
        raise HTTPException(status_code=404, detail="Moto no encontrada")
    for key, value in moto.dict().items():
        setattr(db_moto, key, value)
    db.commit()
    db.refresh(db_moto)
    return db_moto


@app.delete("/motos/{matricula}", tags=["Motos"], response_model=MotoResponse)
def eliminar_moto(matricula: str, db: Session = Depends(get_db)):
    db_moto = db.query(Moto).filter(Moto.matricula == matricula).first()
    if db_moto is None:
        raise HTTPException(status_code=404, detail="Moto no encontrada")
    db.delete(db_moto)
    db.commit()
    return db_moto

@app.delete("/motos/", tags=["Motos"], status_code=204)
def eliminar_todo_inventario_motos(db: Session = Depends(get_db)):
    db.query(Moto).delete()
    db.commit()
    return {"detail": "Todo el inventario de motos ha sido eliminado"}


# Pydantic models para el modelo Barco
class BarcoCreate(BaseModel):
    matricula: str
    marca: str
    modelo: str
    año: int
    capacidad: int

class BarcoResponse(BarcoCreate):
    id: int

    class Config:
        orm_mode = True


# Crear una nueva barco
@app.post("/barcos/", tags=["Barcos"], response_model=BarcoResponse)
def crear_barco(barco: BarcoCreate, db: Session = Depends(get_db)):
    db_barco = Barco(**barco.dict())
    db.add(db_barco)
    db.commit()
    db.refresh(db_barco)
    return db_barco


# Obtener todos los barcos
@app.get("/barcos/", tags=["Barcos"], response_model=List[BarcoResponse])
def obtener_barcos(db: Session = Depends(get_db)):
    return db.query(Barco).all()


# Obtener un barco por matrícula
@app.get("/barcos/{Matricula}", tags=["Barcos"], response_model=BarcoResponse)
def obtener_barco(matricula: str, db: Session = Depends(get_db)):
    barco = db.query(Barco).filter(Barco.matricula == matricula).first()
    if barco is None:
        raise HTTPException(status_code=404, detail="Barco no encontrado")
    return barco


# Actualizar un barco
@app.put("/barcos/{Matricula}", tags=["Barcos"], response_model=BarcoResponse)
def actualizar_barco(matricula: str, barco: BarcoCreate, db: Session = Depends(get_db)):
    db_barco = db.query(Barco).filter(Barco.matricula == matricula).first()
    if db_barco is None:
        raise HTTPException(status_code=404, detail="Barco no encontrado")
    for key, value in barco.dict().items():
        setattr(db_barco, key, value)
    db.commit()
    db.refresh(db_barco)
    return db_barco


# Eliminar un barco
@app.delete("/barcos/{Matricula}", tags=["Barcos"], response_model=BarcoResponse)
def eliminar_barco(matricula: str, db: Session = Depends(get_db)):
    barco = db.query(Barco).filter(Barco.matricula == matricula).first()
    if barco is None:
        raise HTTPException(status_code=404, detail="Barco no encontrado")
    db.delete(barco)
    db.commit()
    return barco
