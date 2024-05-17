from menu import *
from cargardatos import *

datosruta  = "Ejercicio1/datos.json"

datos = cargardatos(datosruta)

while True:
    menu()
    op = seleccion()

    if op == 1:
        print()

    elif op == 2:
        while True:

            carreras()
            op1 = seleccion()

            if op1 == 1:

                print
                
            elif op1 ==2:

                print
            
            elif op1 ==3:

                print

            elif op1 ==4:

                break

    elif op == 3:
        print("Adios")
        break

guardardatos(datos,datosruta)