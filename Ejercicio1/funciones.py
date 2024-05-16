from cargartxt import *


def registrar_empleado(datos):
    datos = dict(datos)
    empleado = {}
    
    empleado["nombre"]= input("ingrese el nombre: ")
    empleado["documento"]= input("ingrese el documento: ")
    empleado["edad"]= int(input("ingrese la edad: "))
    empleado["telefono"]= input("ingrese el telefono: ")
    print("ingrese estado del empelado 1. Contratado")
    estado = int(input(""))
    try:
        if estado == 1:
            empleado["estado"] = "Contratado"
    except ValueError:
        print("opcion invalida")
    else:
        datos["empleado"].append(empleado)
        print("--"*10)
        print("Empleado registrado con extio")
        print("--"*10)
        return datos


def listar_empleado(datos):
    datos = dict(datos)
    while True:
        print("__"*10)
        for i in range(len(["empleado"])):
            print("\n",datos["empleado"][i]["nombre"],"\n",datos["empleado"][i]["documento"],"\n",datos["empleado"][i]["edad"],"\n",datos["empleado"][i]["telefono"],"\n",datos["empleado"][i]["estado"])
            print("__"*10)
        return

def modificar_empledado(datos):
    datos = dict(datos)
    docuemnto = input("ingrese el documento del empleado a mordicar: ")
    for i in range(len(["empleado"])):
        try:
            if datos["empleado"][i]["documento"] == docuemnto:
                datos["empleado"][i]["nombre"] = input("ingrese el nombre: ")
                datos["empleado"][i]["edad"] = int(input("ingrese la edad: "))
                datos["empleado"][i]["telefono"] = input("ingrese el telefono: ")
                print("--"*10)
                print("Empleado registrado con extio")
                print("--"*10)
                return datos
        except ValueError:
            print("--"*10)
            print("Modificacion imbalida")
            print("--"*10)
    
def despedir_empleado(datos):
    datos = dict(datos)
    docuemnto = input("ingrese el documento del empleado a mordicar: ")
    for i in range(len(["empleado"])):
        try:
            if datos["empleado"][i]["documento"] == docuemnto:
                if datos["empleado"][i]["estado"] == "Contratado":
                    despedir = int(input("quiere despedir 1. SI, 2. NO :" ))
                    if despedir == 1:
                        datos["empleado"][i]["estado"] = "Despedido"
                        print("empleado despedido")
                        return datos
                    elif despedir == 2:
                        break
                    
                else:
                    print("--"*10)
                    print("empleado ya esta despedidio")
                    print("--"*10)
        except ValueError:
            print("--"*10)
            print("Modificacion imbalida")
            print("--"*10)

def entrada(datos):
    datos = dict(datos)
    documento = input("ingrese el documento del empleado: ")
    for i in range(len(["empleado"])):
        if documento == ["empleado"][i]["documento"]:
            entradah = int(input("ingrese la hora de la entrada"))
            entradam = int(input("ingrese los minutos de la entrada"))
            nombre = ""

            if entradah > 8 and entradam != 0:
                datos["empleado"][i]["nombre"] == nombre
                mensaje = "entro tarde" 
                guardar_txt(nombre,mensaje,entradah,entradam)
            
                


                
            
            
        

        
