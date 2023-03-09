from Empleado import Empleado
class Analista(Empleado):
    def __init__(self,nombre,salario,metodologia):
        super().__init__(nombre,salario)
        self.metodologia=metodologia
    def calcular_salario(self):
        return self.salario*1.8
    