def crear_pagina():
    """crea un archivo llamado ticket y lo cierra"""
    try:
        archivo = open("logica/parcial/ticket.txt", "x")
        archivo.close
    except:
        pass

def registrar():
    """introduce la cantidad de productos a registrar e identifica si es mayor a 0 y menor a 5"""
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
    """sirve para ingresar y verificar la descripcion de los productos"""
    while True:
        descripcion = input("ingrese una descripcion: ").upper()
        if descripcion:
            return descripcion
        else:
            descripcion == ""
            print("por favor ingrese una descripcion")

def cantidad_de_productos():
    """ingresar cantidad de productos y verifica que no esten vacios ni que sean 0 """
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
    """sirve para ingresar el precio individial de los productos y verifica que sean decimales"""
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
escribir_archivo = open("logica/parcial/ticket.txt", "a")
escribir_archivo.write("\n" + "Ida al supper" + "\n")
for datos in range(ingresar):
    descripcion = nombre()
    escribir_archivo.write(str({"descripcion":descripcion}) + "\n")
    cantidad = cantidad_de_productos()
    escribir_archivo.write(str({"cantidad": cantidad}) + "\n")
    precio_unitario = precio_por_unidad()
    escribir_archivo.write(str({"precio unitario": precio_unitario}) + "\n")
    Subtotal = cantidad * precio_unitario
    escribir_archivo.write(str({"subtotal": Subtotal}) + "\n")
print(Subtotal)
escribir_archivo.close()