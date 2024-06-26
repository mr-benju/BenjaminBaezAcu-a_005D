import json, os

# Enviar mantenedores
# Enviar crud
# importar menu
# Utilizar os
# Reportes

archivoNombre = "biblioteca.json"

def crearAutor():
    id = int(input("Ingrese el nuevo id: ")) # int
    nombre = input("Ingrese el nombre del autor: ")
    nacionalidad = input("Ingrese la nacionalidad: ")
    
    dic = [{
        "AutorID": id,
        "Nombre":nombre,
        "Nacionalidad": nacionalidad
    }]
    
    with open(archivoNombre, "r") as archivo:
        leerJson = json.load(archivo)
        leerJson["Autor"] = dic

        with open(archivoNombre, "w") as guardar:
            json.dump(leerJson,guardar,indent = 1)


def listarAutor():
    with open(archivoNombre, "r") as archivo:
        leerJson = json.load(archivo)
        for i in leerJson:
            print(i)
            for x in leerJson(i):
                print(x)
            






def borrarAutor():
    id = input("Ingrese el id del autor")

    with open(archivoNombre, "r") as archivo:
        leerJson = json.load(archivo)
        if id in leerJson:
            leerJson.pop(id)

        with open(archivoNombre, "w") as borrar:
            json.dump(leerJson,borrar,indent = 4)
            print("¡Borrado exitoso!")

def actualizarAutor():
    with open(archivoNombre, "r") as archivo:
        leerJson = json.load(archivo)
        id = int(input("Ingrese el id: "))
        nombre = input("Ingrese el nombre del autor: ")
        nacionalidad = input("Ingrese la nacionalidad: ")
        dic = leerJson["Autor"]
        for dic in leerJson:
            dic ={
                "AutorID": id,
                "Nombre":nombre,
                "Nacionalidad": nacionalidad
            }

        with open(archivoNombre, "w") as actualizar:
            json.dump(leerJson,actualizar,indent = 1)
actualizarAutor()

def menuMantenedor():

    print("------------------------------")
    print("         MUNDO LIBRO          ")
    print("------------------------------\n")
    print("1.____________________________ Mantenedor de autores")
    print("2.____________________________ Reportes")
    print("3.____________________________ Salir")
    
    opcion = int(input("Ingrese una opcion: "))

    match opcion:
        case 1:
            menu()


def menu(): 
    print("------------------------------------------")
    print("         MANTENEDORES DE AUTORES          ")
    print("----------------------------------------\n")
    print("1.____________________________ Crear autor")
    print("2.____________________________ Listar autores")
    print("3.____________________________  Actualizar autores")
    print("4.____________________________  Borrar autores")
    opcion = int(input("Ingrese una opcion: "))

    match opcion:
        case 1:
           crearAutor()
           menu()
        case 2:
            listarAutor()
            menu()
        case 3:
           actualizarAutor()
           menu()
        case 4:
            borrarAutor()
            menu()






# def reportes():

#opcion salir