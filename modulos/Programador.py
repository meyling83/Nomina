#clase programador. Hereda de Empleado
from modulos.Empleado import Empleado
class Programador(Empleado):
    def __init__(self,nombre,salario,puesto,lenguaje_programacion):
        super().__init__(nombre,salario,puesto)
        self.lenguaje_programacion=lenguaje_programacion
    #funcion para calcular el salario. Si el lenguaje de programacion es python multiplicar por 1.5
    #si es java por 1.3, cualquier otro por 1.2
    def calcular_salario(self):
        if self.lenguaje_programacion.lower()=="python":
            return self.salario*1.5
        elif self.lenguaje_programacion.lower()=="java":
            return self.salario*1.3
        else:
            return self.salario*1.2