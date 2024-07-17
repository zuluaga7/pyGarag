import csv
from Automoviles import Automoviles


class AdminAutomoviles:

    def __init__(self):
        self.automoviles = []
        self.cargar_datos()

    def cargar_datos(self):
        try:
            with open('automoviles.csv', 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    automovil = Automoviles(row['matricula'], row['marca'], row['categoria'], int(row['año']))
                    self.automoviles.append(automovil)
                print("Datos cargados correctamente.")
        except FileNotFoundError:
            print("Archivo de datos no encontrado. Se creará uno nuevo al guardar.")
        except Exception as e:
            print(f"Error al cargar los datos: {e}")

    def agregar_automovil(self):
        while True:
            try:
                matricula = input("Ingrese la matrícula: ")
                if self.buscar_automovil(matricula):
                    print(f"Automóvil con matrícula {matricula} ya existe.")
                    return
                marca = input("Ingrese la marca: ")
                categoria = input("Ingrese la categoría: ")
                año = input("Ingrese el año: ")
                año = int(año)

                automovil = Automoviles(matricula, marca, categoria, año)
                self.automoviles.append(automovil)
                self.guardar_datos()
                print("Automóvil agregado correctamente.")
                break
            except ValueError:
                print("El año debe ser un número entero. Intente nuevamente.")
            except Exception as e:
                print(f"Error inesperado: {e}. Intente nuevamente.")

    def guardar_datos(self):
        try:
            with open('automoviles.csv', 'w', newline='') as f:
                fieldnames = ['matricula', 'marca', 'categoria', 'año']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for automovil in self.automoviles:
                    writer.writerow({
                        'matricula': automovil.matricula,
                        'marca': automovil.marca,
                        'categoria': automovil.categoria,
                        'año': automovil.año
                    })
                print("Datos guardados correctamente.")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def editar_automovil(self):
        matricula = input("Ingrese la matrícula del automóvil a editar: ")
        automovil = self.buscar_automovil(matricula)
        if not automovil:
            print(f"Automóvil con matrícula {matricula} no encontrado.")
            return
        marca = input("Ingrese la nueva marca del automóvil: ")
        categoria = input("Ingrese la nueva categoría del automóvil: ")
        año = input("Ingrese el nuevo año del automóvil: ")
        try:
            año = int(año)
        except ValueError:
            print("El año debe ser un número entero. Intente nuevamente.")
            return
        automovil.marca = marca
        automovil.categoria = categoria
        automovil.año = año
        self.guardar_datos()
        print("Automóvil editado correctamente.")

    def eliminar_automovil(self):
        matricula = input("Ingrese la matrícula del automóvil a eliminar: ")
        automovil = self.buscar_automovil(matricula)
        if not automovil:
            print(f"Automóvil con matrícula {matricula} no encontrado.")
            return
        self.automoviles.remove(automovil)
        self.guardar_datos()
        print("Automóvil eliminado correctamente.")

    def mostrar_automoviles(self):
        if not self.automoviles:
            print("No hay automóviles en el sistema.")
        else:
            for automovil in self.automoviles:
                print(automovil)

    def buscar_automovil(self, matricula=None):
        if not matricula:
            matricula = input("Ingrese la matrícula del automóvil que desea buscar (o 'salir' para cancelar): ")
            if matricula.lower() == 'salir':
                return None
        automovil_encontrado = next((automovil for automovil in self.automoviles if automovil.matricula == matricula),
                                    None)
        if automovil_encontrado:
            print(f"Información del automóvil encontrado:\n{automovil_encontrado}")
        else:
            print(f"No se encontró ningún automóvil con la matrícula {matricula}." + "por favor, continúe con el regisstro.")
        return automovil_encontrado


