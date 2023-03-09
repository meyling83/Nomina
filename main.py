from  modulos.Sistema_Nominas import Sistema_Nominas
from  modulos.Analista import Analista
from  modulos.Programador import Programador
if __name__=="__main__":
    empleados=[]
    accion="s"
    while accion.upper()=="s":
        nombre=input("Entre el nombre")
        cargo=input("Entre A si es analista o P si es programador")
        if(cargo.upper()=="A"):
            metodologia=input("entre la metodologia")
            empleado=Analista(nombre,metodologia)
        elif (cargo.upper()=="P"):
            lenguaje=input("Entre el lenguaje")
            empleado=Programador(nombre,lenguaje)
        empleados.append(empleado)
        accion=input("desea continuar S/N")
    else:
        nominas=Sistema_Nominas()
        nominas.calcular_nominas(empleados)