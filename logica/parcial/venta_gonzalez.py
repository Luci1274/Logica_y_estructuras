def crear_pagina():
    try:
        archivo = open("logica/pacial/ticket.txt", "x")
        archivo.close
    except:
        pass


def registrar():
    while True:
        cantidad_de_productos = input("ingrese la cantidad de productos de arregistrar de 1 a 5: ")
        try:
            cantidad_de_productos = int(cantidad_de_productos) 
            cantidad_de_productos >0 
            cantidad_de_productos <=5
            return cantidad_de_productos
        except ValueError:
            print('Por favor ingrese una cantidad valida')

def nombre():
    while True:
        descripcion = input("ingrese una descripcion: ").upper()
        if descripcion:
            return descripcion
        else:
            descripcion == ""
            print("por favor ingrese una descripcion")

def cantidad_de_productos():
    while True:
        cantidad = input("ingrese la cantidad: ")
        try:
            if cantidad:
                
                return int(cantidad)
            else:
                cantidad == ""
                cantidad == 0
                print("por favor ingresar la cantidad de productos")  
        except:
            print("por favor ingresar la cantidad de productos")

            
def precio_por_unidad():
    while True:
        try: 
            precio_unitario = input("ingrese el precio por unidad: ")
            if precio_unitario:
                precio_unitario = float(precio_unitario)
                precio_unitario > 0
                return float(precio_unitario)
            else:
                precio_unitario == 0
                precio_unitario == ""
                print("ingrese un numero decimal mayor a 0")
        except:
            print("por favor ingrese un flotante")


"""cuerpo princpial"""
print("Bienvenido al super ")
crear_archivo_de_texto = crear_pagina
ingresar = registrar()
descripcion = nombre()
cantidad = cantidad_de_productos()
precio_unitario = precio_por_unidad()
Subtotal = cantidad * precio_unitario
print(Subtotal)
todo = {"descripcion": descripcion  , "cantidad": cantidad, "precio_unitario": precio_unitario,"Subtotal": Subtotal}
try:
    archivo = open("logica/pacial/ticket.txt", "a")
    for mostrar in todo:
        archivo.write("Ida al supper" + str(todo))
    archivo.close()
except:
    print("error desconocido")