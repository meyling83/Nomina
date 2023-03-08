class Empleado:
    def __init__(self,nombre,salario):
        self.nombre=nombre
        self.salario=salario
    def calcular_salario(self):
        return self.salario*1.1