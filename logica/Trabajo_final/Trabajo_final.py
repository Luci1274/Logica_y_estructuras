#Importaciones
from ast import Try
from email import header
import clear
import pandas as pd
from os import listdir
from tabulate import tabulate

#Funciones
def crear_archivo (ruta_1988, ruta_2007, ruta_2016):
    """Esta función lo que hace es crear un archivo que unifica todos los datos, para luego
    abrir los otros archivos en formato de listas, borrando la primera línea y 
    guardar su información en el nuevo"""
    try:
        archivo_nuevo = open("Trabajo_final/destino-produccion-leche-1983-2016.csv", "x")
        archivo_nuevo.close()
    except:
        print("El archivo ya fue creado")
    ruta_1983_2016 = "Trabajo_final/destino-produccion-leche-1983-2016.csv"
    archivo_nuevo = open(ruta_1983_2016, "w+")
    archivo1 = open(ruta_1988, "r").readlines()
    archivo2 = open(ruta_2007, "r").readlines()
    archivo3 = open(ruta_2016, "r").readlines()
    for datos in archivo1:
        archivo_nuevo.writelines(datos)
    archivo_nuevo.write("\n")
    archivo2.pop(0)
    for datos in archivo2:
        archivo_nuevo.writelines(datos)
    archivo3.pop(0)
    for datos in archivo3:
        archivo_nuevo.writelines(datos)
    archivo_nuevo.close
    return ruta_1983_2016
        
def elegir_archivo():
    """Esta función en primera instacia tiene un diccionaria donde están los archvivos 
    que se pueden elegir, luego permite al usuario ongresar el numero que tenga el archivo deseado
    para devolverlo al final"""
    clear.clear()
    separador = "\n"
    archivos = {1:"destino-produccion-leche-1983-1988",2:"destino-produccion-leche-1989-2007",3:"destino-produccion-leche-2008-2016",4:"destino-produccion-leche-1983-2016"}
    while True:
        print(
       " " + "1" + " " + archivos[1] + separador,
        "2" + " " + archivos[2] + separador,
        "3" + " " + archivos[3] + separador,
        "4" + " " + archivos[4] + separador)
        try:
            eleccion = input(separador + "Por favor elija el archivo que más le guste o aprete <0> para salir: ").strip()
            eleccion = int(eleccion)
        except:
            print(separador + "Por favor introduzca uno de los numeros mostrados en pantalla" + separador)
            continue    
        if not eleccion:
                print(separador + "Se a salido con exito" + separador)
                exit()
        elif not eleccion in archivos:
            print(separador + "Por favor selecione uno de los archivos" + separador)
            continue
        else:
            break    
    archivo_elegido = archivos[eleccion]
    return archivo_elegido

def elegir_columna():
    """"""
    separador = "\n"
    columnas_disponibles = {1:"año",2:"mes",3:"producto destino",4:"cantidad por millón"}
    while True:
        print(
        " " + "1" + " " + columnas_disponibles[1] + separador,
        "2" + " " + columnas_disponibles[2] + separador,
        "3" + " " + columnas_disponibles[3] + separador,
        "4" + " " + columnas_disponibles[4] + separador)
        try:
            eleccion = input(separador + "Por favor elija la columna que más le guste o aprete <0> para salir: ").strip()
            eleccion = int(eleccion)
        except:
            print(separador + "Por favor introduzca uno de los numeros mostrados en pantalla" + separador)
            continue    
        if not eleccion:
                print(separador + "Se a salido con exito" + separador)
                exit()
        elif not eleccion in columnas_disponibles:
            print(separador + "Por favor selecione una de las columnas" + separador)
            continue
        else:
            break    
    columna_elegida = columnas_disponibles[eleccion]
    return columna_elegida

def mostrar_años_disponibles(archivo_elegido):
    """"""
    clear.clear()
    años = open(archivo_elegido, "r").readlines()
    años_disponibles = set({})
    for a in años:
        separador = a.split(",")
        años_disponibles.add(separador[2])
    return años_disponibles
        
def mostrar_meses_disponibles(archivo_elegido):
    """"""
    clear.clear()
    meses = open(archivo_elegido, "r").readlines()
    meses_disponibles = set({})
    for a in meses:
        separador = a.split(",")
        meses_disponibles.add(separador[3])
    return meses_disponibles

def mostrar_productos_destino_disponibles(archivo_elegido):
    """"""
    clear.clear()
    productos = open(archivo_elegido, "r").readlines()
    productos_destino_disponibles = set({})
    for a in productos:
        separador = a.split(",")
        productos_destino_disponibles.add(separador[7])
    return productos_destino_disponibles

def mostrar_cantidad_millon_disponibles(archivo_elegido):
    """"""
    clear.clear()
    cantidad = open(archivo_elegido, "r").readlines()
    cantidad_millon_disponibles = set({})
    for a in cantidad:
        separador = a.split(",")
        cantidad_millon_disponibles.add(separador[10])
    return cantidad_millon_disponibles

def opciones_primer_dato(columna_elegida, años_disponibles, meses_disponibles, productos_destino_disponibles, cantidad_millon_disponibles):
    """"""
    clear.clear()
    print("Ahora elegirá de forma más especifica el", columna_elegida)
    while True:
        if columna_elegida == "año":
            print(años_disponibles)
            ingresar = input("Por favor ingrese uno de estos años: ").strip().upper()
            try:
                int(ingresar)
            except:
                print("Por favor ingrese un año valido")
                continue
            if not ingresar:
                print("Por favor ingrese un año ", años_disponibles)
                continue
            elif not ingresar in años_disponibles:
                print("Por favor elija uno de los siguientes años ", años_disponibles)
                continue
            else:
                return ingresar        
        elif columna_elegida == "mes":
            print(meses_disponibles)
            ingresar = input("Por favor ingrese uno de estos meses: ").strip().upper()
            if not ingresar:
                print("Por favor ingrese un mes: ", meses_disponibles)
                continue
            elif not ingresar in meses_disponibles:
                print("Por favor elija uno de los siguientes meses: ", meses_disponibles)
                continue
            else:
                return ingresar
        elif columna_elegida == "producto destino":
            print(productos_destino_disponibles)
            ingresar = input("Por favor ingrese uno de estos productos: ").strip().upper()
            if not ingresar:
                print("Por favor ingrese un producto: ", productos_destino_disponibles)
                continue
            elif not ingresar in productos_destino_disponibles:
                print("Por favor elija uno de los siguientes productos: ", productos_destino_disponibles)
                continue
            else:
                return ingresar
        elif columna_elegida == "cantidad por millon":
            print(cantidad_millon_disponibles)
            ingresar = input("Por favor ingrese uno de estas cantidades: ").strip().upper()
            try:
                float(ingresar)
            except:
                print("Por favor ingrese un valor valido")
                continue
            if not ingresar:
                print("Por favor ingrese una cantidad: ", cantidad_millon_disponibles)
                continue
            elif not ingresar in cantidad_millon_disponibles:
                print("Por favor elija uno de las siguientes cantidades: ", cantidad_millon_disponibles)
                continue
            else:
                return ingresar

def opciones_segundo_dato(archivo_elegido, primer_dato, segunda_columna_elegida):
    """"""
    clear.clear()
    años = set({})
    meses = set({})
    productos_destino = set({})
    cantidad_millon = set({})    
    archivo = open(archivo_elegido, "r").readlines()
    for datos in archivo:
        separador = datos.split(",")
        if primer_dato in datos:
            años.add(separador[2])
            meses.add(separador[3])
            productos_destino.add(separador[7])
            cantidad_millon.add([10])
    while True:
        if segunda_columna_elegida == "año":
            print(años)
            ingresar = input("Por favor ingrese uno de estos años: ").strip().upper()
            try:
                int(ingresar)
            except:
                print("Por favor ingrse un año valido")
                continue
            if not ingresar or not ingresar in años:
                print("Por favor ingrese un año ", años)
                continue
            else:
                return ingresar
        elif segunda_columna_elegida == "mes":
            print(meses)
            ingresar = input("Por favor ingrese uno de estos meses: ").strip().upper()
            if not ingresar or not ingresar in meses:
                print("Por favor ingrese un mes ", meses)
                continue
            else:
                return ingresar
        elif segunda_columna_elegida == "producto destino":
            print(productos_destino)
            ingresar = input("Por favor ingrese uno de estos productos: ").strip().upper()
            if not ingresar or not ingresar in productos_destino:
                print("Por favor ingrese un producto ", productos_destino)
                continue
            else:
                return ingresar
        elif segunda_columna_elegida == "cantidad por millon":
            print(meses)
            ingresar = input("Por favor ingrese uno de estas cantidades: ").strip().upper()
            try:
                float(ingresar)
            except:
                print("Por favor ingrese un valor valido")
                continue
            if not ingresar or not ingresar in cantidad_millon:
                print("Por favor ingrese una cantidad ", cantidad_millon)
                continue
            else:
                return ingresar

def procesar_un_dato(archivo_elegido, columna_elegida, primer_dato):
    """"""
    clear.clear()
    año = []
    mes = []
    producto_destino = []
    unidad_med = []
    cantidad_millon = []
    datos_procesados = {"año": año, "mes": mes, "producto destino": producto_destino , "unidad med.": unidad_med, "cantidad millon": cantidad_millon}
    archivo = open(archivo_elegido, "r").readlines()
    for dato in archivo:
        separador = dato.split(",")
        if columna_elegida == "año":
            if primer_dato in dato:
                año.append(separador[2])
                mes.append(separador[3])
                producto_destino.append(separador[7])
                unidad_med.append(separador[8])
                cantidad_millon.append(separador[10])
        elif columna_elegida == "mes":
            if primer_dato in dato:
                año.append(separador[2])
                mes.append(separador[3])
                producto_destino.append(separador[7])
                unidad_med.append(separador[8])
                cantidad_millon.append(separador[10])
        elif columna_elegida == "producto destino":
            if primer_dato in dato:
                año.append(separador[2])
                mes.append(separador[3])
                producto_destino.append(separador[7])
                unidad_med.append(separador[8])
                cantidad_millon.append(separador[10])
        elif columna_elegida == "cantidad por millon":
            if primer_dato in dato:
                año.append(separador[2])
                mes.append(separador[3])
                producto_destino.append(separador[7])
                unidad_med.append(separador[8])
                cantidad_millon.append(separador[10])
    return datos_procesados

def procesar_dos_dato(archivo_elegido, columna_elegida, segunda_columna_elegida, primer_dato, segundo_dato):
    """"""
    clear.clear()
    dato1 = []
    dato2 = []
    unidad_med = []
    datos_procesados = {"dato1": dato1, "dato2": dato2, "unidad med": unidad_med}
    archivo = open(archivo_elegido, "r").readlines()
    for dato in archivo:
        separador = dato.split(",")
        if columna_elegida == "año" or segunda_columna_elegida == "año":
            if primer_dato in dato or segundo_dato in dato:
                dato1.append(separador[2])
                dato2.append(separador[2])
        elif columna_elegida == "mes" or segunda_columna_elegida == "mes":
            if primer_dato in dato or segundo_dato in dato:
                dato1.append(separador[3])
                dato2.append(separador[3])
        elif columna_elegida == "producto destino" or segunda_columna_elegida == "producto destino":
            if primer_dato in dato or segundo_dato in dato:
                dato1.append(separador[7])
                dato2.append(separador[7])
        elif columna_elegida == "cantidad por millon" or segunda_columna_elegida == "cantidad por millon":
            if primer_dato in dato or segundo_dato in dato:
                dato1.append(separador[10])
                dato2.append(separador[10])
        unidad_med.append(separador[8])            
    return datos_procesados
    
def tabla(datos_procesados):
    """"""
    clear.clear()
    datos_procesados
    df = pd.DataFrame(datos_procesados)
    ascendente = input("Desea verlo de forma ascendente? S o N: ")
    if not ascendente or ascendente == "N":
        df = df.sort_values("cantidad millon", ascending = False)    
    else:
        df = df.sort_values("cantidad millon", ascending = True)
    top = input("Desea ver un top ten o 10? s o n: ").upper().strip()
    if not top or top == "N":
        
        print(tabulate(df, showindex=False, tablefmt='fancy_grid'))
    else:
        df = df.reset_index(drop=True)
        df.drop(df.index[11:100], inplace=True)
        print("\nTop 10\n""\n", tabulate(df, tablefmt='fancy_grid'), "\n")
    pausa = input("Precione <ENTER> para continuar")
    return

def tabla_dos_datos(datos_procesados):
    """"""
    clear.clear()
    datos_procesados
    df = pd.DataFrame(datos_procesados)
    ascendente = input("Desea verlo de forma ascendente? S o N: ")
    if not ascendente or ascendente == "N":
        df = df.sort_values("dato2", ascending = False)    
    else:
        df = df.sort_values("dato2", ascending = True)
    top = input("Desea ver un top ten o 10? s o n: ").upper().strip()
    if not top or top == "N":
        
        print(tabulate(df, showindex=False, tablefmt='fancy_grid'))
    else:
        df = df.reset_index(drop=True)
        df.drop(df.index[11:100], inplace=True)
        print("\nTop 10\n""\n", tabulate(df, tablefmt='fancy_grid'), "\n")
    pausa = input("Precione <ENTER> para continuar")
    return

#Cuerpo principal
ruta_1988 = "Trabajo_final/destino-produccion-leche-1983-1988.csv"
ruta_2007 = "Trabajo_final/destino-produccion-leche-1989-2007.csv"
ruta_2016 = "Trabajo_final/destino-produccion-leche-2008-2016.csv"
ruta_1983_2016 = crear_archivo(ruta_1988, ruta_2007, ruta_2016)
while True:
    archivo_elegido = elegir_archivo()
    columna_elegida = elegir_columna()
    archivo_elegido = "Trabajo_final/" + archivo_elegido + ".csv"
    preguntar_segunda_columna = input("desea elegir otra columna? s o n ").strip().upper()
    if not preguntar_segunda_columna or preguntar_segunda_columna == "N":
        años_disponibles = mostrar_años_disponibles(archivo_elegido)
        meses_disponibles = mostrar_meses_disponibles(archivo_elegido)
        productos_destino_disponibles = mostrar_productos_destino_disponibles(archivo_elegido)
        cantidad_millon_disponibles = mostrar_cantidad_millon_disponibles(archivo_elegido)
        while True:   
            primer_dato = opciones_primer_dato(columna_elegida, años_disponibles, meses_disponibles, productos_destino_disponibles, cantidad_millon_disponibles)
            datos_procesados = procesar_un_dato(archivo_elegido, columna_elegida, primer_dato)
            tabla(datos_procesados)
            break
    else:
      while True:
        segunda_columna_elegida = elegir_columna()
        if columna_elegida == segunda_columna_elegida:
            print("No puedes elegir 2 veces el mismo dato, por favor elija otro")
            continue
        else:
            años_disponibles = mostrar_años_disponibles(archivo_elegido)
            meses_disponibles = mostrar_meses_disponibles(archivo_elegido)
            productos_destino_disponibles = mostrar_productos_destino_disponibles(archivo_elegido)
            cantidad_millon_disponibles = mostrar_cantidad_millon_disponibles(archivo_elegido)
            while True:    
                primer_dato = opciones_primer_dato(columna_elegida, años_disponibles, meses_disponibles, productos_destino_disponibles, cantidad_millon_disponibles)
                segundo_dato = opciones_segundo_dato(segunda_columna_elegida, años_disponibles, meses_disponibles, productos_destino_disponibles, cantidad_millon_disponibles)
                datos_procesados = procesar_dos_dato(archivo_elegido, columna_elegida, segunda_columna_elegida, primer_dato, segundo_dato)
                break    
    pregunta = input("Quieres realizar otra tabla s o n").upper().strip()
    if pregunta == "N" or not pregunta:
        print("Muchas gracias por tu tiempo")
        exit()
    else:
        continue