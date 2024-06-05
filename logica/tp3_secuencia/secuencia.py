import os
def clearConsole():
    print("\n" * 2)

def ingresar_dato(mensaje):
    """permite el ingreso de un dato y valida que sea numerico"""
    while True:
        numero = input(mensaje)
        try:
            numero = int(numero)
            break     
        except:
            print("Tipo de dato incorrecto")
            continue
    return numero   

def mostrar_secuencia(s):
    for interador in s:
        print(interador)
    return

def crear_pagina():
    try:
        archivo = open("logica/tp3_secuencia/secuencia.txt", "x")
        archivo.close
    except:
        pass

    
"""cuerpo principal del programa"""
crear = crear_pagina

valor_inicial = ingresar_dato("ingrese un valor numerico inicial: ")
valor_final = ingresar_dato("ingrese un valor numerico final: ")
salto = ingresar_dato("ingrese el salto: ")

secuencia = range(valor_inicial, valor_final, salto)
mostrar_secuencia(secuencia)



archivo = open("logica/tp3_secuencia/secuencia.txt", "a")
archivo.write("\n")
for valor in secuencia:
    archivo.write(str(valor) + "-")
    clearConsole
archivo.close()