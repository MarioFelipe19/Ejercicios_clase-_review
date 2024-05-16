from menu import *
from cargar_datos import *
from funciones import *

datos_json = "Ejercicio1/datos.json"

datos = cargar_datos(datos_json)

while True:

    menu()
    op = pedir_opcion()
    
    if op == 1:
        datos = registrar_empleado(datos)
    elif op == 2:
        listar_empleado(datos)
    elif op == 3:
        datos = modificar_empledado(datos)
    elif op == 4:
        datos = despedir_empleado(datos)
    elif op == 5:
        entrada(datos)
    elif op == 6:
        print()
    elif op == 7:
        print("Adios!")
        break
    else:
        print("opcion invalida")


guardar_datos(datos, datos_json)
    