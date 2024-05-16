


def menu():
    print("")
    print("=="*20)
    print("Menu empresa")
    print("1. Registrar empleado")
    print("2. Listar todos los empleados")
    print("3. Modificar empleados")
    print("4. Despedir empleados")
    print("5. Registrar entrada empleados")
    print("6. Registrar salida de empleado")
    print("7. Salir")
    print("=="*20)

def pedir_opcion():
    try:
        print("=="*20)
        op = int(input("Ingrese el numero de la opcion: "))
        print("=="*20)
        return op
    except Exception:
        print("valro invalido")
