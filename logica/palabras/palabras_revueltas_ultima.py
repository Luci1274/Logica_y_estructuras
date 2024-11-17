from random import choice, shuffle
import pandas as pd
from os import listdir, system , chdir, getcwd
def crear_archivo(ruta_de_jugador):
    """Crea un archivo para guardar la informacion de los jugadores o participantes"""
    try:
        archivo_jugador = open(ruta_de_jugador, "x")
        print("Creaste un archivo")
    except:
        print(" El archivo ya fue creado")
    return

def temas(ruta_temas):
    """muestra una lista de temas"""
    lista_de_temas = listdir(ruta_temas)
    lista = list([])
    chdir(ruta_temas)
    medio = "\n"
    for i, temas in enumerate(lista_de_temas):
        temas_a_elegir = (f"{i}:{temas}")
        lista.append(temas_a_elegir), medio
    print(lista,"\n")
    return lista


def elegir_tema(temas_a_elegir,ruta_de_jugador):
    while True:
        elegir_tema = input("Ingrese el numero del tema: ").strip()
        if not elegir_tema:
            print("Por favor elija un tema")
            continue
        elif elegir_tema:
            tema_elegido = temas_a_elegir[int(elegir_tema)]
            tema_elegido[2:]
            print("El tema elegido fue: ",tema_elegido)
            with open(ruta_de_jugador,"a")as dato_jugador:
                dato_jugador.write(str(tema_elegido[2:-1]) + ",")
            ruta_tema_elegido = getcwd()+ "/" + str(tema_elegido[2:])
            print(ruta_tema_elegido)
            return ruta_tema_elegido
        else:
            print("error elija uno de estos numeros")

def promedio(ruta_tema_elegido):
    tema_elegido = open(ruta_tema_elegido,"r").readlines()
    minimo = 0
    maximo = 0
    for numero in range(len(tema_elegido)):
        if numero > maximo:
            maximo = int(numero)
        elif numero > minimo < maximo:
            numero = minimo
    resta = maximo - minimo
    medio = resta / 2
    print(minimo,maximo,medio)
    return ruta_tema_elegido,medio, maximo

def mesclar_palabra(ruta_tema_elegido, ruta_de_jugador,promedio):
    tema_elegido =open(ruta_tema_elegido,"r").readline().splitlines()
    contador = 0
    while True:
        if contador != 3:
            dificultad = input("Escribe una dificultas <FACIL> o <DIFICIL>: ").strip().upper()
            if not dificultad:
                print("Por favor elija una")
                continue
            elif dificultad == "FACIL":
                    palabra = choice(tema_elegido).upper()
                    if len(palabra) <= int(promedio):
                        x = list(palabra)
                        shuffle(x)
                        palabra_elegida = palabra
                        with open(ruta_de_jugador,"a")as dato_jugador:
                            dato_jugador.write(palabra_elegida)
                            dato_jugador.write(",")
                        return palabra_elegida, x
                    else:
                        continue
            elif dificultad == "DIFICIL":
                while contador:
                    palabra = choice(tema_elegido).upper()
                    if len(palabra) >= int(promedio):
                        x = list(palabra)
                        shuffle(x)
                        palabra_elegida = palabra
                        with open(ruta_de_jugador,"a")as dato_jugador:
                            dato_jugador.write(palabra_elegida + ",")
                        return palabra_elegida, x
                    else:
                        continue
        else:
            return    

def juego_1(palabra_elegida, palabra_desordenada, ruta_de_jugador):
    intentos = 4
    print(palabra_desordenada)
    puntos = intentos * len(palabra_elegida)
    while True:
        resolver = input("Por favor ordena esta palabra: ").upper().strip()
        if resolver == palabra_elegida:
            puntos
            print("\nMuy bien",palabra_elegida)
            return
        elif intentos == 1 :
            print("\nperdiste (T_T) la palabra era:", palabra_elegida, "Tus puntso fueron", puntos)
            return
        elif resolver != palabra_elegida:
            intentos -= 1
            print("\nerror vuelva a intentar ordenar:", palabra_desordenada, "te quedan", intentos)
            continue
        else:
            print("fin del juego")
            with open(ruta_de_jugador,"a")as dato_jugador:
                    dato_jugador.write(puntos)
            return
    
def ranking(ruta_de_jugadores):
    mejores_jugadores = open(ruta_de_jugadores,"r").readline()
    mejores_jugadores.split(",")
    nombre = mejores_jugadores[0]
    tema = mejores_jugadores[1]
    puntos = mejores_jugadores[5]

    pausa = input("Precione <ENTER> para continuar")
    return



#Cuerpo principal#
#palabras/temas/marcas de autos.lst
ruta_de_jugador = "archivo_jugador.csv"
ruta_temas = "temas"
crear_archivo(ruta_de_jugador)
while True:
    nombre_jugador = input("Bienvenido por favor ingrese su nombre o aprete <ENTER> para salir: ").strip()
    if len(nombre_jugador) == 0:
        print("\nSe a salido con exito")
        exit()
    elif nombre_jugador:
        with open(ruta_de_jugador,"a")as dato_jugador:
            dato_jugador.write(nombre_jugador + ",")
        lista = temas(ruta_temas)
        break
    else:
        print("\nPor favor ingrese un nombre\n")
        continue
ruta_tema_elegido = elegir_tema(lista,ruta_de_jugador)
ruta_tema_elegido,medio, maximo = promedio(ruta_tema_elegido)
contador = 0
while True:
    if contador != 3:
        palabra_elegida, x = mesclar_palabra(ruta_tema_elegido, ruta_de_jugador,medio)
        juego_1(palabra_elegida, x,  ruta_de_jugador)
        contador +=1
        continue
    else:
        ranking(ruta_de_jugador)
        exit()