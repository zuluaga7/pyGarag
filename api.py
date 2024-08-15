from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from base_de_datos import SessionLocal, engine
from modelos import Base, Automovil

app = FastAPI()
"""@app.get("/",tags=["Prueba pipe"])
def root():
    return "hola"""


# Crear las tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)


# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Pydantic models
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


# Endpoints
@app.post("/automoviles/", response_model=AutomovilResponse)
def create_automovil(automovil: AutomovilCreate, db: Session = Depends(get_db)):
    db_automovil = Automovil(**automovil.dict())
    db.add(db_automovil)
    db.commit()
    db.refresh(db_automovil)
    return db_automovil


@app.get("/automoviles/{matricula}", response_model=AutomovilResponse)
def read_automovil(matricula: str, db: Session = Depends(get_db)):
    db_automovil = db.query(Automovil).filter(Automovil.matricula == matricula).first()
    if db_automovil is None:
        raise HTTPException(status_code=404, detail="Automóvil no encontrado")
    return db_automovil


@app.put("/automoviles/{matricula}", response_model=AutomovilResponse)
def update_automovil(matricula: str, automovil: AutomovilCreate, db: Session = Depends(get_db)):
    db_automovil = db.query(Automovil).filter(Automovil.matricula == matricula).first()
    if db_automovil is None:
        raise HTTPException(status_code=404, detail="Automóvil no encontrado")
    for key, value in automovil.dict().items():
        setattr(db_automovil, key, value)
    db.commit()
    db.refresh(db_automovil)
    return db_automovil


@app.delete("/automoviles/{matricula}", response_model=AutomovilResponse)
def delete_automovil(matricula: str, db: Session = Depends(get_db)):
    db_automovil = db.query(Automovil).filter(Automovil.matricula == matricula).first()
    if db_automovil is None:
        raise HTTPException(status_code=404, detail="Automóvil no encontrado")
    db.delete(db_automovil)
    db.commit()
    return db_automovil