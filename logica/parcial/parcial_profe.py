def dibujar_encabezado():
    '''Imprimir un encabezado en pantalla.'''
    print('#' * 50)
    print('VENTA POR CAJA RAPIDA (máximo 5 items)'.center(50))
    print('#' * 50)
    return

def ingresar_producto():
    '''Ingresa y valida la descripcion del producto.'''
    while True:
        descripcion = input(" Ingrese la descripción del producto: ").strip()
        if not descripcion:
            print("\nError! Debe tipear algo.")
            continue
        return descripcion.upper()

def ingresar_cantidad():
    '''Ingresa y valida la cantidad.'''
    while True:
        try: 
            cantidad = int(input(" Cantidad: "))
            if cantidad != 0:
                return cantidad
            else:
                print("\nError! Debe ingresar un número entero positivo o negativo.")
        except ValueError:
            print("\nError! La cantidad debe ser ingresada en números.")
    
def ingresar_precio_unitario():
    '''Ingresar y validar precio unitario.'''
    while True:
        try:
            precio_unitario = float(input(" Precio por unidad: "))
            if precio_unitario > 0:
                return precio_unitario
            else: 
                print("\nError! El producto debe tener un precio.")
        except ValueError:
            print("\nError! El precio debe estar registrado en números.") 

def registrar_item_venta(nro_item):
    '''Registrar el item compuesto por producto, cantidad y precio unitario.'''
    while True:
        print("\nItem #", nro_item)
        descripcion = ingresar_producto()
        cantidad = ingresar_cantidad()
        precio_unitario = ingresar_precio_unitario()
        item = descripcion, cantidad, precio_unitario
        print(" Subtotal: ", cantidad * precio_unitario)
        confirma_item = input("Confirma el registro de este item (S/N)? ").strip().lower()
        if confirma_item == 's':
            return item
        
def mostrar_venta(detalle_venta):
    '''Mostrar la venta formateada en base a la lista de tuplas.'''
    cantidad_items = len(detalle_venta)
    unidades = 0
    total_venta = 0
    print('-'*50)
    for renglon in detalle_venta:
        descripcion, cantidad, precio_unitario = renglon[0], renglon[1], renglon[2]
        subtotal = cantidad * precio_unitario
        unidades += cantidad
        total_venta += subtotal
        print(descripcion, cantidad, precio_unitario, subtotal)
    print('-'*50)
    print('Items:', cantidad_items)
    print('Unidades:', unidades)
    print('Total de la venta:', total_venta)
    return

def guardar_ticket(detalle_venta):
    '''Registra la venta en un archivo txt.'''
    tkt =  open("ticket.txt", "w")
    tkt.write('TICKET DE VENTA\n')
    cantidad_items = len(detalle_venta)
    unidades = 0
    total_venta = 0
    tkt.write('-' * 50 + '\n')
    for renglon in detalle_venta:
        descripcion, cantidad, precio_unitario = renglon[0], renglon[1], renglon[2]
        unidades += cantidad
        subtotal = cantidad * precio_unitario
        total_venta += subtotal
        tkt.write(descripcion + ' ' + str(cantidad) + ' ' + str(precio_unitario) + ' ' + str(subtotal) + '\n')
    tkt.write('-'*50 + '\n')
    tkt.write('Items: ' + str(cantidad_items) + '\n')
    tkt.write('Unidades: ' + str(unidades) + '\n')
    tkt.write('Total de la venta:' + str(total_venta) + '\n')    
    tkt.close()
    print('Ticket archivado OK')
    return


#################################
# cuerpo principal del programa #
#################################
venta = []
numero_item = 1
dibujar_encabezado()
while numero_item <= 5:
    venta.append(registrar_item_venta(numero_item))
    otro_item = input("Otro item (S/N)? ").strip().lower()
    if otro_item == 's':
        numero_item += 1
    elif otro_item == 'n':
        break
mostrar_venta(venta)
confirma_venta = input("\nConfirma la venta (S/N)? ").strip().lower()
if confirma_venta == 's':
    guardar_ticket(venta)