import modulos.Sistema_Nominas
import modulos.Analista as analista
import modulos.Programador as programador
if __name__=="__main"__:
    empleados=[]
    accion="s"
    while accion.upper()=="s":
        nombre=input("Entre el nombre")
        cargo=input("Entre A si es analista o P si es programador")
        if(cargo.upper()=="A"):
            metodologia=input("entre lametodologia")
            empleado=analista.Analista(nombre,metodologia)
        elif (cargo.upper()=="P"):
            lenguaje=input("Entre el lenguaje")
            empleado=programador.Programador(nombre,lenguaje)
        empleados.append(empleado)
        accion=input("desea continuar S/N")
    else:
        nominas=Sistema_Nominas()
        nominas.calcular_nominas(empleados)