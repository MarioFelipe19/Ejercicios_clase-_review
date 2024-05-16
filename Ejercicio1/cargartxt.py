file = open("Ejercicio1/registro.txt" , "r")
print(file.read)
file.close

def guardar_txt(nombre,mensaje,entradah,entradam):
    mensajec = nombre+ mensaje + entradah +":"+ entradam
    with     open("registro.txt", "a") as file:
        file.write( mensajec + '\n')
    file.close