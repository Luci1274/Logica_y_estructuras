while True:
    try:
        numero1 = int(input("ingresa un numero: "))
        break
    except SyntaxError:
        print("Por favor ingrese un numero")

if numero1 >= 0 and numero1 <= 10:
    print(numero1, " El numero se encuentra entre 0 y 10 ")
elif numero1 <=10:
    print(numero1, " El numero se encuentra entre 0 y 10 ")
else:
    print("El numero no se encuentra entre 0 y 10")

if numero1 == 11:
    print(numero1, " El numero se encuentra entre 11 y 20 ")
elif numero1 <=20:
    print(numero1, " El numero se encuentra entre 11 y 20 ")
else:
    print("El numero no se encuentra entre 11 y 20")

if numero1 == 21:
    print(numero1, " El numero se encuentra entre 21 y 30 ")
elif numero1 <=30:
    print(numero1, " El numero se encuentra entre 21 y 30 ")
else:
    print("El numero no se encuentra entre 21 y 30")