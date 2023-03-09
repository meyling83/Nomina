class Analista:
    def __init__(self,nombre,salario,metodologias):
        super().__init__(nombre,salario)
        self.metodologias=metodologias
    def calcular_salario(self):
        return self.salario*1.8
    