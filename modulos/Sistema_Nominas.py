class Sistema_Nominas:
    def calcular_nominas(self,empleados):
        print("Calculando nominas")
        print("==============================================")
      
        for emp in empleados:
             #si el empleado es analista imprimo la metodologia y el nombre
            if emp.puesto=="analista":
                print(f"Nomina para: {emp.nombre} - {emp.metodologia}")
            #si el empleado es programador imprimo nombre y lenguaje de programacion
            elif emp.puesto=="programador":
                 print(f"Nomina para: {emp.nombre} - {emp.lenguaje_programacion}")

            print(f"-$:{emp.calcular_salario()}")
            print("")

