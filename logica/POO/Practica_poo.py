class Persona:
    """representa a personas en general"""
    especie = "Mamifero"
    def __init__(self, sujeto, apellido, edad):
        
        print(f"Mi nombre es {sujeto}, mí apellido es {apellido}, y mi edad es {edad}")
        self.sujeto = sujeto
        self.apellido = apellido
        self.edad = edad
    def habla(self):
        print(f"y este es mí mascota")

class Animal:
    def __init__(self,especie,nombre,edad):
        print(f"Es un {especie}, su nombre es {nombre}, y su edad es {edad}")
        self.especie = especie
        self.nombre = nombre
        self.edad = edad
    


while True:
    sujeto = input("cual es tu nombre")
    apellido = input("ingrese su apellido")
    edad = input("ingrese su edad")

    sujeto = Persona(sujeto,apellido,edad)
    reintentar = input("quieres reintentar?")
    if reintentar == "si" or reintentar == "SI":
        continue
    else:
        break
while True:
    mascota = input("tienes mascota?").upper()
    if mascota == "si" or mascota == "SI":
        sujeto.habla()
        especie = input("especie de su mascota")
        nombre = input("nombre de la mascota")
        edad = input("edad de la mascota")
        mascota = Animal(especie,nombre,edad)
        exit()
    else:
        break