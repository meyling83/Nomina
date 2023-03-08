import Empleado
class Programador(Empleado):
    def __init__(self,nombre,salario,lenguaje_programacion):
        super().__init__(nombre,salario)
        self.lenguaje_programacion=lenguaje_programacion
    def calcular_salario(self):
        pass