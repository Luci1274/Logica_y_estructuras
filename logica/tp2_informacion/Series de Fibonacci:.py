# Series de Fibonacci:
# la suma de dos elementos define el siguiente

def ingreasar_tope():
    """solicita al operador un nro para la serie de fibo"""
    numero = input("ingrese un valor numerico limite: ")
    return int(numero)

def fibo(limite): # devuelve la serie de Fibonacci hasta un cierto limite
    sucesion = []
    a, b = 0, 1
    while a < limite:
        sucesion.append(a) # ver abajo
        a, b = b, a+b
        return sucesion
"""cuerpo principal del programa"""    
t = ingreasar_tope()
r = fibo(t)
print(r)