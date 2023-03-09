class Empleado:
    def __init__(self,nombre,salario,puesto):
        self.nombre=nombre
        self.puesto=puesto
        self.salario=30000
    def calcular_salario(self):
        return self.salario*1.1
