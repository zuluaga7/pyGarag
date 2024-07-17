class Automoviles:

    def __init__(self, matricula, marca, categoria, año):
        self._matricula = matricula
        self._marca = marca
        self._categoria = categoria
        self._año = año

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, value):
        self._matricula = value

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        self._categoria = value



    @property
    def año(self):
        return self._año

    @año.setter
    def año(self, value):
        if value >= 0:
            self._año = value
        else:
            raise ValueError("El año no es correcto")

    def __str__(self):
        return f"Marca: {self.marca}, Matricula: {self._matricula}, Categoria: {self.categoria}, Año: {self._año}"
