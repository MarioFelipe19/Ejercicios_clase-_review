import json

def cargardatos(archivo):
    datos = {}
    with open(archivo, "r") as file:
        datos = json.load(file)
    return datos

def guardardatos(datos,archivo):
    datos = dict(datos)
    diccionario = json.dumps(datos, indent=4)
    file = open(archivo, "w")
    file.write(diccionario)
    file.close