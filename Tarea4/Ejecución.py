from Arrays import Array
from Trabajadores import Trabajadores

print("EL PROGRAMA SE VE MEJOR EN PANTALLA COMPLETA")
#Abriendo archivo
datos = open("junio.dat","rt")
#Leyendo cada renglon del archivo y seccionandolo
lista = Array(15)
for i in range(0,15,1):
    #Se hace slicing para separar los datos de cada renglon
    renglon = datos.readline().strip("\n").split(",")#strip(), simple elimina espacios vacios
    #Se guardan los rennglones con los elemntos separados en un array
    lista.set_item(renglon,i)

trabajadores = Array(14)
for i in range(1,lista.get_length()):
    #Pasando los datos de losta en un array de objetos Trabajadores
    empleado=Trabajadores(lista.get_item(i)[0],lista.get_item(i)[1],lista.get_item(i)[2],lista.get_item(i)[3],lista.get_item(i)[4],lista.get_item(i)[5],lista.get_item(i)[6])
    trabajadores.set_item(empleado,i-1)

#Imprimiendo objetos con sus respectivos Atributos
print("\n\n\n----------------------MOSTRANDO LISTA COMPLETA DE TRABAJADORES------------------------")
for i in range(trabajadores.get_length()):
    print(trabajadores.get_item(i).to_string())

#Calcuñando sueldo de cada empleado
print("\n\n\n-------------------------MOSTRANDO LISTA COMPLETA DE SUELDOS--------------------------")
for i in range(trabajadores.get_length()):
    antiguedad = int(2020 - int(trabajadores.get_item(i).get_año_ingreso()))#Tiempo de antuguedad
    prestaciones = (((float(trabajadores.get_item(i).get_s_base())/100)*3)*antiguedad)#prestaciones

    sueldo_extra=float(int(trabajadores.get_item(i).get_h_extra())*276.5)#sueldo por horas extra
    sueldo_total=float(int(trabajadores.get_item(i).get_s_base())+sueldo_extra+prestaciones)#sueldo total
    print(f"El trabajador: {trabajadores.get_item(i).get_nombre()}, por horas extras obtuvo {sueldo_extra}, sus prestaciones son: {prestaciones}, y su sueldo total de {sueldo_total}")

#Obteniendo datos de mayor y menor antiguedad
menor_a=int(trabajadores.get_item(0).get_año_ingreso())
mayor_a=int(trabajadores.get_item(0).get_año_ingreso())
for i in range(trabajadores.get_length()):
    if (menor_a < int(trabajadores.get_item(i).get_año_ingreso())):
        menor_a=int(trabajadores.get_item(i).get_año_ingreso())
    elif (mayor_a > int(trabajadores.get_item(i).get_año_ingreso())):
        mayor_a=int(trabajadores.get_item(i).get_año_ingreso())

print("\n\n\n-------------------------MOSTRANDO TRABAJADORES CON MAS ANTIGUEDAD--------------------------")
for i in range(trabajadores.get_length()):
    if (mayor_a == int(trabajadores.get_item(i).get_año_ingreso())):
        antiguedad = int(2020 - int(trabajadores.get_item(i).get_año_ingreso()))
        print(f"{trabajadores.get_item(i).get_nombre()} ingresó el {trabajadores.get_item(i).get_año_ingreso()}, por tanto tiene {antiguedad} años de antiguedad")

print("\n\n\n-----------------------MOSTRANDO TRABAJADORES CON MENOS ANTIGUEDAD--------------------------")
for i in range(trabajadores.get_length()):
    if (menor_a == int(trabajadores.get_item(i).get_año_ingreso())):
        antiguedad = int(2020 - int(trabajadores.get_item(i).get_año_ingreso()))
        print(f"{trabajadores.get_item(i).get_nombre()} ingresó el {trabajadores.get_item(i).get_año_ingreso()}, por tanto tiene {antiguedad} años de antiguedad")

print("\nEL PROGRAMA SE VE MEJOR EN PANTALLA COMPLETA")
