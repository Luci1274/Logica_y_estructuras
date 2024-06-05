cartel = input("Introduzca un texto: ").upper().strip(" ")
largo = len(cartel)
caracter_arriba = ("┳━━━")
caracter_bajo =   ("┻━━━")
vacio =""
import os
def clearConsole():
    print("\n" * 150)

while True: 
    if cartel:
        print(caracter_arriba * len(cartel)+ "┳")
        print("┃ ", end="")
        for letras in (cartel):
            print(letras, end=" ┃ ")
            print(end="")
        print()
        print(caracter_bajo * len(cartel)+ "┻")
        preciona_enter = input("Pulse <Enter> para retornar: ")
        clearConsole, print("\n" * 150)
        cartel = input("Introduzca un texto o pulse <Enter> para salir: ").upper().strip(" ")
        
    else: 
        cartel == ""
        print("Tomando un descanso".upper())
        break