from modulos.Sistema_Nominas import Sistema_Nominas
from modulos.Analista import Analista
from modulos.Programador import Programador
from modulos.Empleado import Empleado
if __name__=="__main__":
    empleados=[]
    accion="s"
    #entrada de los datos de los empleados. 
    #Si es programador se crea un objeto de la clase programador con sus datos. 
    #o si es analista, se crea un objeto de la clase analista
    while accion.upper()=="S":
        nombre=input("Entre el nombre")
        salario=float(input("entre el salario"))
        cargo=input("Entre A si es analista o P si es programador")
        if(cargo.upper()=="A"):
            metodologia=input("entre la metodologia")
            empleado=Analista(nombre,salario,"analista",metodologia)
        elif (cargo.upper()=="P"):
            lenguaje=input("Entre el lenguaje")
            empleado=Programador(nombre,salario,"programador",lenguaje)
        else:
            empleado=Empleado(nombre,salario,cargo)
        empleados.append(empleado)
        accion=input("desea continuar S/N")
    #al terminar la introduccion de los empleados se crea el objeto nominas y se imprime la nomina
    else:
        nominas=Sistema_Nominas()
        nominas.calcular_nominas(empleados)