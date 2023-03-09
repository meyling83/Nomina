import modulos.Empleado as empleado
import modulos.Analista as analista
import modulos.Programador as Programador

class Sistema_Nominas:
    def calcular_nominas(self,empleados):
        print("Calculando nominas")
        print("==============================================")
        for emp in empleados:
            print(f"Nomina para: {emp.nombre} - {emp.lenguaje_programacion}")
            print(f"-$:{emp.calcular_salario()}")
            print("")

