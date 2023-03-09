class Sistema_Nominas:
    def calcular_nominas(self,empleados):
        print("Calculando nominas")
        print("==============================================")
        for emp in empleados:
            if emp.puesto=="analista":
                print(f"Nomina para: {emp.nombre} - {emp.metodologia}")
            elif emp.puesto=="programador":
                 print(f"Nomina para: {emp.nombre} - {emp.lenguaje_programacion}")

            print(f"-$:{emp.calcular_salario()}")
            print("")

