"""from sqlalchemy.orm import Session
from modelos import Automovil  # El modelo SQLAlchemy que definimos antes
from base_de_datos import SessionLocal  # Sesión de la base de datos


def eliminar_automovil():
    db = SessionLocal()

    matricula = input("Ingrese la matrícula del automóvil que desea eliminar: ")
    automovil = db.query(Automovil).filter(Automovil.matricula == matricula).first()

    if automovil:
        db.delete(automovil)
        db.commit()
        print("Automóvil eliminado exitosamente.")
    else:
        print("Automóvil no encontrado.")

    db.close()


class AdminAutomoviles:

    def agregar_automovil(self):
        matricula = input("Ingrese la matrícula: ")
        marca = input("Ingrese la marca: ")
        categoria = input("Ingrese la categoría: ")
        año = int(input("Ingrese el año: "))

        # Crear una nueva sesión de base de datos
        db = SessionLocal()

        # Crear una instancia del modelo Automovil
        nuevo_auto = Automovil(matricula=matricula, marca=marca, categoria=categoria, año=año)

        # Guardar en la base de datos
        db.add(nuevo_auto)
        db.commit()
        db.refresh(nuevo_auto)
        db.close()

    def mostrar_automoviles(self):
        # Crear una nueva sesión de base de datos
        db = SessionLocal()

        # Obtener todos los automóviles
        automoviles = db.query(Automovil).all()
        for auto in automoviles:
            print(f"Matrícula: {auto.matricula}, Marca: {auto.marca}, Categoría: {auto.categoria}, Año: {auto.año}")

        db.close()

    def buscar_automovil(self, matricula):
        db = SessionLocal()

        # Buscar automóvil por matrícula
        automovil = db.query(Automovil).filter(Automovil.matricula == matricula).first()
        if automovil:
            print(
                f"Matrícula: {automovil.matricula}, Marca: {automovil.marca}, Categoría: {automovil.categoria}, Año: {automovil.año}")
        else:
            print("Automóvil no encontrado.")

        db.close()

    def editar_automovil(self):
        db = SessionLocal()

        matricula = input("Ingrese la matrícula del automóvil que desea editar: ")
        automovil = db.query(Automovil).filter(Automovil.matricula == matricula).first()

        if automovil:
            automovil.marca = input("Ingrese la nueva marca: ")
            automovil.categoria = input("Ingrese la nueva categoría: ")
            automovil.año = int(input("Ingrese el nuevo año: "))
            db.commit()
            print("Automóvil editado exitosamente.")
        else:
            print("Automóvil no encontrado.")

        db.close()"""

