class Empleado:
    def __init__(self,nombre,salario,puesto):
        self.nombre=nombre
        self.puesto=puesto
        self.__salario=salario
    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self,value):
        if value<=0:
            print("El salario tiene que ser mayor que 0")
        else:
            self.__salario=value
    def calcular_salario(self):
        return self.__salario*1.1
