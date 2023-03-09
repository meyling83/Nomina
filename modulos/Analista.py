#clase analista, hereda de Empleado
from modulos.Empleado import Empleado
class Analista(Empleado):
    def __init__(self,nombre,salario,puesto,metodologia):
        super().__init__(nombre,salario,puesto)
        self.metodologia=metodologia
    #funcion que calcula el salario del analista multiplicando por 1.8
    def calcular_salario(self):
        return self.salario*1.8