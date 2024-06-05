import os
def clearConsole():
    print("\n" * 13)

def cantidad_de_usuarios():
    while True:    
        try:
            numero_de_usuarios = int(input("ingrese la cantida dad de usuarios de arregistrar: "))
            return int(numero_de_usuarios)
            break
        except ValueError:
                print('Por favor ingrese un numero')

def Ingresar_nombre():
    """Ingresa el nombre de la persona con virtiendolo en una tupla"""
    Nombre = input("Ingrese un Nombre: ").upper().strip(" ")
    Apellido = input("Ingrese un Apellido: ").upper().strip(" ")
    return [Nombre, Apellido]
    

def Ingresar_edad():
    """Ingresar la edad del usuario para luego convertirlo en un entero """
    while True:
        try:
            edad = input("Ingrese una edad menor a 100: ")
            edad == int
            return int(edad)
            break
        except ValueError:
            print("Ingrese una edad")

def afinidad():
    genero = input("ingrese su genero: ")
    return genero

def Fecha_de_nacimiento():
    """Ingresar la fecha de nacimiento del usuario y cinvertirlo en una cadena"""
    fecha = input("Ingrese su fecha de nacimiento: ")
    return str(fecha)

def informacion(resultado):
    resultados = {"nombre y apellido":nombre_y_apellido, "edad": edad, 
            "fecha de nacimiento": fecha, "genero": genero}
    return(resultados)

def Continuar():
    Continuar = input("¿Quieres continuar? si, Para salir precione <enter>: ")
    while True:
        if Continuar:
            Continuar == "SI" or Continuar =="si"
            return Continuar
        else:
            Continuar != "SI" or Continuar!= "si"
            Continuar == ""
            print("Muchas gracias por participar")
            break


cantidad = cantidad_de_usuarios()
if cantidad == 1:
    nombre_y_apellido = Ingresar_nombre()
    edad = Ingresar_edad()
    fecha = Fecha_de_nacimiento()
    genero = afinidad()
    clearConsole()
    print(informacion("resultados"))
elif cantidad == 0:
    print("Dejate de joder")
else:
    while cantidad >=2 <= 10:
        nombre_y_apellido = Ingresar_nombre()
        edad = Ingresar_edad()
        fecha = Fecha_de_nacimiento()
        genero = afinidad()
        clearConsole()
        print(informacion("resultados"))
        Siguiente = Continuar()
        if Siguiente == "Si" or Continuar == "si":
            todo = nombre_y_apellido, edad, fecha, genero
        else:
            Siguiente
            print("muchas gracias por su participacion")
            break