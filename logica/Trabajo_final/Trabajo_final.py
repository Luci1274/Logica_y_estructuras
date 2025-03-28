#Importaciones
from os import getcwd, listdir, mkdir
from types import NoneType
import clear
import pandas as pd
from tabulate import tabulate

#Funciones
def crear_archivo ():
    """Esta función lo que hace es crear un archivo que unifica todos los datos"""
    try:
        archivo_nuevo = open("Trabajo_final/destino-produccion-leche-1983-2016.csv", "x")
        archivo_nuevo.close()
    except:
        print("El archivo ya fue creado")
    ruta_1988 = str(ruta_general) + "/Trabajo_final/destino-produccion-leche-1983-1988.csv"
    ruta_2007 = str(ruta_general) + "/Trabajo_final/destino-produccion-leche-1989-2007.csv"
    ruta_2016 = str(ruta_general) + "/Trabajo_final/destino-produccion-leche-2008-2016.csv"
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

def elegir_columna():
    """Esta funcion nos permite elegir la columna por la cual deseamos realizar filtrado y utiliza la libreria tabulate para mostrar las opciones"""
    linea_separadora = "-" * 65
    separador = "\n"
    columnas_disponibles = {1:"año",2:"mes",3:"producto destino",4:"cantidad por millón"}
    muestra = [[1, "año"], [2, "mes"], [3, "producto destino"], [4, "cantidad por millón"], [0, "Presione para salir"]]
    while True:
        print(tabulate(muestra, tablefmt = 'fancy_grid'))
        try:
            print(linea_separadora * 2)
            eleccion = input(separador + "Por favor elija la columna que más le guste o presione <0> para salir: ").strip()
            eleccion = int(eleccion)
        except:
            print(linea_separadora * 2, separador + "Por favor introduzca uno de los indices mostrados en pantalla" + separador, linea_separadora * 2)
            input("Por favor precione <ENTER>")
            clear.clear()
            continue    
        if not eleccion:
                print(linea_separadora * 2, separador + "Se a salido con exito" + separador, linea_separadora * 2)
                exit()
        elif not eleccion in columnas_disponibles:
            print(linea_separadora * 2, separador + "Por favor introduzca uno de los indices mostrados en pantalla" + separador, linea_separadora * 2)
            input("Por favor precione <ENTER>")
            clear.clear()
        else:
            break    
    columna_elegida = columnas_disponibles[eleccion]
    return columna_elegida

def procesar_primera_columna_elegida_mostrar_opciones(cuarto_archivo, columna_elegida):
    """Esta funcion procesa el archivo por la columna elegida y muestra las opciones disponibles utilizando el la libreria tabulate"""
    clear.clear()
    linea_separadora = "-" * 65
    salto = "\n"
    muestra = []
    archivo = open(cuarto_archivo, "r").readlines()
    print(linea_separadora, salto, "Ahora elegirá de forma más especifica el/la", columna_elegida, salto, linea_separadora)
    while True:
        if columna_elegida == "año":
            conjunto_años = set({})
            for años in archivo:
                separador = años.split(",")
                conjunto_años.add(separador[2])
            conjunto_años.remove("año")
            conjunto_años = sorted(conjunto_años)
            indice = 1
            opciones_primer_dato = {}
            for años_disponibles in conjunto_años:
                opciones_primer_dato[indice] = años_disponibles
                muestra.append([str(indice), años_disponibles])
                indice += 1
            print(tabulate(muestra, tablefmt = 'fancy_grid'))
            return opciones_primer_dato, muestra
        elif columna_elegida == "mes":
            opciones_primer_dato = set({})
            for meses in archivo:
                separador = meses.split(",")
                opciones_primer_dato.add(separador[3])
            opciones_primer_dato.remove("mes")
            for Mostrar_meses in range(1, 13):
                muestra.append([str(Mostrar_meses)])
            print(tabulate(muestra, tablefmt = 'fancy_grid'))
            return opciones_primer_dato, muestra
        elif columna_elegida == "producto destino":
            conjunto_productos = set({})
            for productos in archivo:
                separador = productos.split(",")
                conjunto_productos.add(separador[7])
            conjunto_productos.remove("producto_destino")
            indice = 1
            opciones_primer_dato = {}
            for productos_disponibles in conjunto_productos:
                opciones_primer_dato[indice] = productos_disponibles
                muestra.append([str(indice), productos_disponibles])
                indice += 1
            print(tabulate(muestra, tablefmt = 'fancy_grid'))
            return opciones_primer_dato, muestra
        elif columna_elegida == "cantidad por millón":
            conjunto_cantidad_millon = set({})
            for cantidad_millon in archivo:
                separador = cantidad_millon.split(",")
                conjunto_cantidad_millon.add(separador[10][:-1])
            try:
                conjunto_cantidad_millon.remove("cantidad_por_millon")
            except:
                pass
            indice = 1
            opciones_primer_dato = {}
            pausa = [518, 1036, 1554, 2072, 2590, 3108, 3626, 3976]
            for millon_disponible in conjunto_cantidad_millon:
                opciones_primer_dato[indice] = millon_disponible
                muestra.append([str(indice), float(millon_disponible)])
                indice += 1
                if indice in pausa:
                    print(tabulate(muestra, tablefmt = 'fancy_grid'), salto, linea_separadora * 2)
                    corte = input("Presione <ENTER> para ver las demás opciones o precione 0 para saltar la muestra: ").strip()
                    clear.clear()
                    if corte == "0":
                        muestra.clear()
                        opciones_primer_dato.clear()
                        indice = 1
                        for millon_disponible in conjunto_cantidad_millon:
                            opciones_primer_dato[indice] = millon_disponible
                            muestra.append([str(indice), float(millon_disponible)])
                            indice += 1
                        return opciones_primer_dato, muestra 
                    else:
                        clear.clear()
            return opciones_primer_dato, muestra

def elegir_primer_dato(columna_elegida, opciones_primer_dato, muestra):
    """En esta funcion podemos elegir el dato que querramos"""
    linea_separadora = "-" * 65
    salto = "\n"
    print(linea_separadora * 2, salto, "Ahora debe eligir de forma más especifica el/la", columna_elegida, salto, linea_separadora * 2)
    while True:
        if columna_elegida == "año":
            ingresar = input("Por favor ingrese el indice del año deseado: ").strip()
            try:
                ingresar = int(ingresar)
            except:
                print(linea_separadora * 2, salto, "Por favor ingrese un indice valido", salto, linea_separadora * 2)
                input("Presione <ENTER>")
                clear.clear()
                print(salto,tabulate(muestra, tablefmt = 'fancy_grid'), salto)
                continue
            if not ingresar or not ingresar in opciones_primer_dato:
                print(linea_separadora * 2, salto, "Por favor ingrese un indice valido: ", salto, linea_separadora * 2)
                input("Presione <ENTER>")
                clear.clear()
                print(tabulate(muestra, tablefmt = 'fancy_grid'), salto)
                continue
            else:
                dato_elegido = opciones_primer_dato[ingresar]
                return dato_elegido        
        elif columna_elegida == "mes":
            ingresar = input("Por favor ingrese uno de estos meses: ")
            try:
                int(ingresar)
            except:
                print(linea_separadora * 2, salto, "Por favor ingrese uno de los meses mostrados", salto, linea_separadora * 2)
                input("Presione <ENTER>")
                print(linea_separadora)
                clear.clear()
                print(tabulate(muestra, tablefmt = 'fancy_grid'), salto)
                continue
            if not ingresar or not ingresar in opciones_primer_dato:
                print(linea_separadora * 2, salto, "Por favor ingrese un mes de los antes mostrados: ", salto, linea_separadora * 2)
                input("Presione <ENTER>")
                clear.clear()
                print(tabulate(muestra, tablefmt = 'fancy_grid'), salto)
                continue
            else:
                dato_elegido = ingresar
                return dato_elegido
        elif columna_elegida == "producto destino":
            ingresar = input("Por favor ingrese el numero de uno de estos productos: ")
            try:
                ingresar = int(ingresar)
            except:
                clear.clear()
                print(linea_separadora * 2, salto, "Por favor el numero del producto", salto, linea_separadora * 2)
                input("Presione <ENTER>")
                clear.clear()
                print(tabulate(muestra, tablefmt = 'fancy_grid'), salto)
                continue
            if not ingresar or not ingresar in opciones_primer_dato:
                print(linea_separadora * 2, salto, "Por favor ingrese un producto: ", salto, linea_separadora * 2)
                input("Presione <ENTER>")
                clear.clear()
                print(tabulate(muestra, tablefmt = 'fancy_grid'), salto)
                continue
            else:
                dato_elegido = opciones_primer_dato[ingresar]
                return dato_elegido
        elif columna_elegida == "cantidad por millón":
            volver_mostrar_muestra = []
            print(linea_separadora * 2, salto, "Por favor ingrese un numero del 1 hasta el", len(muestra), ": " , salto, linea_separadora * 2)
            ingresar = input()
            try:
                ingresar = int(ingresar)
            except:
                clear.clear()
                print(linea_separadora * 2, salto, "Por favor ingrese el numero de la cantidad " , salto, linea_separadora * 2)
                input("Presione <ENTER>")
                clear.clear()
                pausa = [518, 1036, 1554, 2072,2590, 3108, 3626, 3976]
                indice = 1
                for millon_disponible in muestra:
                    volver_mostrar_muestra.append(millon_disponible)
                    indice += 1
                    if indice in pausa:
                        print(tabulate(volver_mostrar_muestra, tablefmt = 'fancy_grid'), salto, linea_separadora * 2)
                        corte = input("Presione <ENTER> para ver las demás opciones o precione 0 para saltar la muestra: ").strip()
                        clear.clear()
                        if corte == "0":
                            clear.clear()
                            break
                continue
            if not ingresar or not ingresar in opciones_primer_dato:
                print(linea_separadora * 2, salto, "Por favor ingrese una cantidad: ", salto, linea_separadora * 2)
                input("Presione <ENTER>")
                clear.clear()
                pausa = [518, 1036, 1554, 2072, 2590, 3108, 3626, 3976]
                indice = 1
                for millon_disponible in muestra:
                    volver_mostrar_muestra.append(millon_disponible)
                    indice += 1
                    if indice in pausa:
                        print(tabulate(volver_mostrar_muestra, tablefmt = 'fancy_grid'), salto, linea_separadora * 2)
                        corte = input("Presione <ENTER> para ver las demás opciones o precione 0 para saltar la muestra: ")
                        clear.clear()
                        if corte == "0":
                            break
                continue
            else:
                dato_elegido = opciones_primer_dato[ingresar]
                return dato_elegido

def procesar_segunda_columna_elegida_mostrar_opciones(cuarto_archivo, dato_elegido, segunda_columna_elegida):
    """Esta funcion recopila y los datos de la segunda columna elegida y utiliza como filtro al primer dato elegido, ademas de utilizar tabulate para mostrar los resultados"""
    clear.clear()
    linea_separadora = "-" * 65
    salto = "\n"
    muestra = []
    archivo = open(cuarto_archivo, "r").readlines()
    print(linea_separadora * 2, salto, "Ahora elegirá de forma más especifica el/la", segunda_columna_elegida, salto, linea_separadora * 2)
    while True:
        if segunda_columna_elegida == "año":
            conjunto_años = set({})
            for años in archivo:
                if dato_elegido in años:
                    separador = años.split(",")
                    conjunto_años.add(separador[2])
            try:
                conjunto_años.remove("año")
            except:
                pass
            conjunto_años = sorted(conjunto_años)
            indice = 1
            opciones_segundo_dato = {}
            for años_disponibles in conjunto_años:
                opciones_segundo_dato[indice] = años_disponibles
                muestra.append([str(indice), años_disponibles])
                indice += 1
            print(tabulate(muestra, tablefmt = 'fancy_grid'), salto)
            return opciones_segundo_dato, muestra
        elif segunda_columna_elegida == "mes":
            opciones_segundo_dato = set({})
            for meses in archivo:
                if dato_elegido in meses:
                    separador = meses.split(",")
                    opciones_segundo_dato.add(separador[3])
            try:
                opciones_segundo_dato.remove("mes")
            except:
                pass
            for mostrar_meses in opciones_segundo_dato:
                muestra.append([int(mostrar_meses)])
            muestra.sort()
            str(muestra)
            print(tabulate(muestra, tablefmt = 'fancy_grid'))
            return opciones_segundo_dato, muestra
        elif segunda_columna_elegida == "producto destino":
            conjunto_productos = set({})
            for productos in archivo:
                if dato_elegido in productos:
                    separador = productos.split(",")
                    conjunto_productos.add(separador[7])
            try:
                conjunto_productos.remove("producto_destino")
            except:
                pass
            indice = 1
            opciones_segundo_dato = {}
            for productos_disponibles in conjunto_productos:
                opciones_segundo_dato[indice] = productos_disponibles
                muestra.append([str(indice), productos_disponibles])
                indice += 1
            print(tabulate(muestra, tablefmt = 'fancy_grid'))
            return opciones_segundo_dato, muestra
        elif segunda_columna_elegida == "cantidad por millón":
            conjunto_cantidad_millon = set({})
            opciones = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
            for cantidad_millon in archivo:
                separador = cantidad_millon.split(",")
                if not dato_elegido in opciones:
                    if dato_elegido in cantidad_millon: 
                        conjunto_cantidad_millon.add(separador[10])
                elif dato_elegido in opciones:
                    if not separador[3] == dato_elegido:
                        pass
                    else:
                        conjunto_cantidad_millon.add(separador[10])     
            try:
                conjunto_cantidad_millon.remove("cantidad_por_millon\n")
            except:
                pass
            indice = 1
            opciones_segundo_dato = {}
            for millon_disponible in conjunto_cantidad_millon:
                opciones_segundo_dato[indice] = millon_disponible
                muestra.append([str(indice), millon_disponible])
                indice += 1
            print(tabulate(muestra, tablefmt = 'fancy_grid'), salto)
            return opciones_segundo_dato, muestra

def elegir_segundo_dato(segunda_columna_elegida, opciones_segundo_dato, muestra):
    """Esta funcion recopila datos que estén relacionados con el primer dato que elegimos 
    y además nos permite elegir un dato especifico para filtrar"""
    clear.clear()
    linea_separadora = "-" * 65
    salto = "\n"
    while True:
        print(linea_separadora * 2, salto, "Ahora debe de elegir de forma más especifica el/la", segunda_columna_elegida, salto, linea_separadora * 2)
        print(tabulate(muestra, tablefmt = 'fancy_grid'), salto)
        if segunda_columna_elegida == "año":
            ingresar = input("Por favor ingrese uno de estos años: ").strip()
            try:
                ingresar = int(ingresar)
            except:
                print(linea_separadora * 2, salto, "Por favor ingrese un año valido", salto, linea_separadora * 2)
                input("Presione <ENTER>")
                clear.clear()
                continue
            if not ingresar or not ingresar in opciones_segundo_dato:
                print(linea_separadora * 2, salto, "Por favor ingrese un indice: ", salto, linea_separadora * 2)
                input("Presione <ENTER>")
                clear.clear()
                continue
            else:
                segundo_dato_elegido = opciones_segundo_dato[ingresar]
                return segundo_dato_elegido
        elif segunda_columna_elegida == "mes":
            ingresar = input("Por favor ingrese uno de estos meses: ")
            try:
                int(ingresar)
            except:
                print(linea_separadora * 2, salto, "Por favor ingrese uno de los meses mostrados", salto, linea_separadora * 2)
                input("Presione <ENTER>")
                clear.clear()
                continue
            if not ingresar or not ingresar in opciones_segundo_dato:
                print(linea_separadora * 2, salto, "Por favor ingrese un mes de los antes mostrados: ", salto, linea_separadora * 2)
                input("Presione <ENTER>")
                clear.clear()
                continue
            else:
                segundo_dato_elegido = ingresar
                return segundo_dato_elegido
        elif segunda_columna_elegida == "producto destino":
            ingresar = input("Por favor ingrese el numero de uno de estos productos: ")
            try:
                ingresar = int(ingresar)
            except:
                clear.clear()
                print(linea_separadora * 2, salto, "Por favor el numero del producto", salto, linea_separadora * 2)
                input("Presione <ENTER>")
                clear.clear()
                continue
            if not ingresar or not ingresar in opciones_segundo_dato:
                print(linea_separadora * 2, salto, "Por favor ingrese un producto: ", salto, linea_separadora * 2)
                input("Presione <ENTER>")
                clear.clear()
                continue
            else:
                segundo_dato_elegido = opciones_segundo_dato[ingresar]
                return segundo_dato_elegido
        elif segunda_columna_elegida == "cantidad por millón":
            print(linea_separadora * 2, salto, "Por favor ingrese un numero del 1 hasta el", len(muestra), ": ", salto, linea_separadora * 2)
            volver_mostrar_muestra = []
            ingresar = input()
            try:
                ingresar = int(ingresar)
            except:
                clear.clear()
                print(linea_separadora, salto, "Por favor ingrese el numero de la cantidad", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                continue
            if not ingresar or not ingresar in opciones_segundo_dato:
                print(linea_separadora, salto, "Por favor ingrese una cantidad: ", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
            else:
                segundo_dato_elegido = opciones_segundo_dato[ingresar]
                return segundo_dato_elegido

def procesar_archivo_por_un_dato(cuarto_archivo, columna_elegida, dato_elegido):
    """Esta funcion recopila todos los datos que estén relacionados con el elegido,
    los agrega una lista especifica y por ultimo devuelve un diccionario"""
    clear.clear()
    año = []
    mes = []
    producto_destino = []
    unidad_med = []
    cantidad_millon = []
    datos_procesados = {"año": año, "mes": mes, "producto destino": producto_destino , "unidad med.": unidad_med, "cantidad millon": cantidad_millon}
    archivo = open(cuarto_archivo, "r").readlines()
    for dato in archivo:
        separador = dato.split(",")
        if columna_elegida == "año":
            if dato_elegido in dato:
                año.append(separador[2])
                mes.append(separador[3])
                producto_destino.append(separador[7])
                unidad_med.append(separador[8])
                cantidad_millon.append(float(separador[10]))
        elif columna_elegida == "mes":
            if dato_elegido in separador[3]:
                if not separador[3] == dato_elegido:
                    pass
                else:
                    año.append(separador[2])
                    mes.append(separador[3])
                    producto_destino.append(separador[7])
                    unidad_med.append(separador[8])
                    cantidad_millon.append(float(separador[10]))
        elif columna_elegida == "producto destino":
            if dato_elegido in dato:
                año.append(separador[2])
                mes.append(separador[3])
                producto_destino.append(separador[7])
                unidad_med.append(separador[8])
                cantidad_millon.append(float(separador[10]))
        elif columna_elegida == "cantidad por millón":
            if dato_elegido in dato:
                año.append(separador[2])
                mes.append(separador[3])
                producto_destino.append(separador[7])
                unidad_med.append(separador[8])
                cantidad_millon.append(float(separador[10]))
    return datos_procesados

def procesar_archivo_por_dos_datos(cuarto_archivo, columna_elegida, segunda_columna_elegida, dato_elegido, segundo_dato_elegido):
    """Esta funcion recopila datos relacionados a las elecciones anteriores y devuelve un diccionario"""
    clear.clear()
    dato1 = []
    dato2 = []
    unidad_med = []
    cantidad_millon = []
    archivo = open(cuarto_archivo, "r").readlines()
    if columna_elegida != "cantidad por millón" and segunda_columna_elegida != "cantidad por millón":
        datos_procesados = {columna_elegida: dato1, segunda_columna_elegida: dato2, "unidad med.": unidad_med, "cantidad millon": cantidad_millon}
        if columna_elegida != "mes" and segunda_columna_elegida != "mes":
            for dato in archivo:
                separador = dato.split(",")
                if dato_elegido in dato and segundo_dato_elegido in dato:
                    if columna_elegida == "año":
                        dato1.append(separador[2])
                    elif columna_elegida == "producto destino":
                        dato1.append(separador[7])
                    if segunda_columna_elegida == "año":
                        dato2.append(separador[2])
                    elif segunda_columna_elegida == "producto destino":
                        dato2.append(separador[7])
                    if True:
                        unidad_med.append(separador[8])
                        cantidad_millon.append(float(separador[10]))
            return datos_procesados
        elif columna_elegida == "mes" or segunda_columna_elegida == "mes":
            for dato in archivo:
                separador = dato.split(",")
                if dato_elegido in dato and segundo_dato_elegido in dato:
                    if columna_elegida == "mes":
                        if not separador[3] == dato_elegido:
                            pass
                        else:
                            dato1.append(separador[3])
                        if segunda_columna_elegida == "año":
                            if not separador[3] == dato_elegido:
                                pass
                            else:
                                dato2.append(separador[2])
                        elif segunda_columna_elegida == "producto destino":
                            if not separador[3] == dato_elegido:
                                pass
                            else:
                                dato2.append(separador[7])
                        if True:
                            if not separador[3] == dato_elegido:
                                pass
                            else:
                                unidad_med.append(separador[8])
                                cantidad_millon.append(float(separador[10]))
                    else:
                        if not separador[3] == segundo_dato_elegido:
                            pass
                        else:
                            dato2.append(separador[3])
                        if columna_elegida == "año":
                            if not separador[3] == segundo_dato_elegido:
                                pass
                            else:
                                dato1.append(separador[2])
                        elif columna_elegida == "producto destino":
                            if not separador[3] == segundo_dato_elegido:
                                pass
                            else:
                                dato1.append(separador[7])
                        if True:
                            if not separador[3] == segundo_dato_elegido:
                                pass
                            else:
                                unidad_med.append(separador[8])
                                cantidad_millon.append(float(separador[10]))
            return datos_procesados
    elif columna_elegida == "cantidad por millón":
        datos_procesados = {columna_elegida: dato1, "unidad med.": unidad_med, segunda_columna_elegida: dato2}
        if segunda_columna_elegida != "mes":
            for dato in archivo:
                separador = dato.split(",")
                if dato_elegido in dato and segundo_dato_elegido in dato:
                    unidad_med.append(separador[8])
                    dato1.append(float(separador[10]))
                if segunda_columna_elegida == "año":
                    if dato_elegido in dato and segundo_dato_elegido in dato:
                        dato2.append(separador[2])
                elif segunda_columna_elegida == "producto destino":
                    if dato_elegido in dato and segundo_dato_elegido in dato:
                        dato2.append(separador[7])
            return datos_procesados
        else:
            for dato in archivo:
                separador = dato.split(",")
                if dato_elegido in dato and segundo_dato_elegido in dato:
                    if not separador[3] == dato_elegido and not separador[3] == segundo_dato_elegido:
                        pass
                    else:
                        unidad_med.append(separador[8])
                        dato1.append(float(separador[10]))
                        dato2.append(separador[3])
            return datos_procesados
    elif segunda_columna_elegida == "cantidad por millón":
        datos_procesados = {columna_elegida: dato1, segunda_columna_elegida: dato2, "unidad med.": unidad_med}
        for dato in archivo:
            separador = dato.split(",")
            if columna_elegida == "mes":
                if dato_elegido in dato and segundo_dato_elegido in dato:
                    if not separador[3] == dato_elegido and not separador[3] == segundo_dato_elegido:
                        pass
                    else:
                        dato1.append(separador[3])
                        unidad_med.append(separador[8])
                        dato2.append(float(separador[10]))
            else:
                if columna_elegida == "año":
                    if dato_elegido in dato and segundo_dato_elegido in dato:
                        dato1.append(separador[2])
                elif columna_elegida == "producto destino":
                    if dato_elegido in dato and segundo_dato_elegido in dato:
                        dato1.append(separador[7])
                if dato_elegido in dato and segundo_dato_elegido in dato:
                    unidad_med.append(separador[8])
                    dato2.append(float(separador[10]))
        return datos_procesados

def crear_mostrar_tabla_extensa(datos_procesados):
    """Esta funcion nos permite visualizar una tabla utilizando la libreria pandas para crear un Dataframe y la libreria tabulate para la visualizacion"""
    linea_separadora = "-" * 65
    salto = "\n"
    clear.clear()
    df = pd.DataFrame(datos_procesados)
    try:    
        print(linea_separadora * 2)
        ascendente = input("Desea verlo de forma ascendente? S o N: ")
        print(linea_separadora * 2)
        if not ascendente or ascendente == "N":
            df = df.sort_values("cantidad millon", ascending = False)    
        else:
            df = df.sort_values("cantidad millon", ascending = True)
        print(linea_separadora * 2)
        top = input("Desea verlo en un top? s o n: ").upper().strip()
        print(linea_separadora * 2)
        if not top or top == "N":
            clear.clear()
            print(tabulate(df, showindex = False, tablefmt = 'fancy_grid', headers = ["año", "mes", "producto destino", "unidad med.", "cantidad por millon"]), salto)
        else:
            while True:
                tops_disponibles = {1: 10, 2: 50, 3: 100}
                muestra_tops_disponibles = [["1", 10], ["2", 50], ["3", 100]]
                print(tabulate(muestra_tops_disponibles, tablefmt = 'fancy_grid'))
                elegir_top = input("Ingrese el numero del top que desee ver: ")
                print(linea_separadora * 2)
                try:
                    elegir_top = int(elegir_top)
                except:
                    clear.clear()
                    print(linea_separadora * 2, salto,"Por favor elija uno de los numeros de adelante", salto, linea_separadora * 2)
                    continue
                if not elegir_top or not elegir_top in tops_disponibles:
                    print(linea_separadora * 2, salto, "Por favor elija uno de los numeros de adelante", salto, linea_separadora * 2)
                    continue
                else:
                    break
            if elegir_top == 1:
                df = df.reset_index(drop = True)
                df.index = df.index + 1
                df.drop(df.index[10:6000], inplace = True)
                clear.clear()
                print(linea_separadora, salto * 2, "Top 10",salto, linea_separadora * 2)
                print(tabulate(df, tablefmt = 'fancy_grid', headers = ["año", "mes", "producto destino", "unidad med.", "cantidad por millon"]))
            elif elegir_top == 2:
                df = df.reset_index(drop = True)
                df.index = df.index + 1
                df.drop(df.index[50:6000], inplace = True)
                clear.clear()
                print(linea_separadora * 2, salto, "Top 50",salto, linea_separadora * 2)
                print(tabulate(df, tablefmt = 'fancy_grid', headers = ["año", "mes", "producto destino", "unidad med.", "cantidad por millon"]))
            else:
                df = df.reset_index(drop = True)
                df.index = df.index + 1
                df.drop(df.index[100:6000], inplace = True)
                clear()
                print(linea_separadora * 2, salto, "Top 100",salto, linea_separadora * 2)
                print(tabulate(df, tablefmt = 'fancy_grid', headers = ["año", "mes", "producto destino", "unidad med.", "cantidad por millon"]))
        print(linea_separadora)
        pausa = input("Precione <ENTER> para continuar")
        print(linea_separadora)
    except:
        print(linea_separadora * 2, salto, "No se puede mostrar la tabla de la forma pedida, por ende se mostrara de forma normal", salto, linea_separadora * 2)
        print(tabulate(df, showindex = False, tablefmt = 'fancy_grid', headers = ["año", "mes", "producto destino", "unidad med.", "cantidad por millon"]))
    return df

def crear_mostrar_tabla_corta(datos_procesados, columna_elegida, segunda_columna_elegida):
    """Esta funcion nos permite visualizar una tabla utilizando la libreria pandas para crear un Dataframe y la libreria tabulate para la visualizacion"""
    clear.clear()
    linea_separadora = "-" * 65
    salto = "\n"
    datos_procesados
    df = pd.DataFrame(datos_procesados)
    try:
        if columna_elegida != "cantidad por millón" and segunda_columna_elegida != "cantidad por millón":
            print(linea_separadora * 2)
            ascendente = input("Desea verlo de forma ascendente? S o N: ")
            print(linea_separadora * 2)
            if not ascendente or ascendente == "N":
                df = df.sort_values( "cantidad millon", ascending = False)    
            else:
                df = df.sort_values("Cantidad millon", ascending = True)
                print(linea_separadora * 2)
        elif columna_elegida == "cantidad por millón" and segunda_columna_elegida != "cantidad por millón":
            clear.clear()
            print(tabulate(df, showindex = False, tablefmt = 'fancy_grid', headers = [columna_elegida, "Forma de medida" , segunda_columna_elegida]), salto)
            print(linea_separadora * 2)
            pausa = input("Precione <ENTER> para continuar")
            print(linea_separadora * 2)
            return df
        else:
            clear.clear()
            print(tabulate(df, showindex = False, tablefmt = 'fancy_grid', headers = [columna_elegida, segunda_columna_elegida, "Forma de medida"]), salto)
            print(linea_separadora * 2)
            pausa = input("Precione <ENTER> para continuar")
            print(linea_separadora * 2)
            return df

        top = input("Desea verlo en un top? s o n: ").upper().strip()
        print(linea_separadora * 2)
        if not top or top == "N":
            print(tabulate(df, showindex = False, tablefmt = 'fancy_grid', headers = [columna_elegida, segunda_columna_elegida, "Forma de medida", "cantidad por millon"]))
        else:
            while True:
                tops_disponibles = {1: 10, 2: 50, 3: 100}
                muestra_tops_disponibles = [["1", 10], ["2", 50], ["3", 100]]
                print(tabulate(muestra_tops_disponibles, tablefmt = 'fancy_grid'))
                elegir_top = input("Ingrese el numero del top que desee ver: ")
                print(linea_separadora * 2)
                try:
                    elegir_top = int(elegir_top)
                except:
                    clear.clear()
                    print(linea_separadora * 2, salto, "Por favor elija uno de los numeros de adelante", salto, linea_separadora * 2)
                    continue
                if not elegir_top or not elegir_top in tops_disponibles:
                    print(linea_separadora * 2, salto, "Por favor elija uno de los numeros de adelante", salto, linea_separadora * 2)
                    continue
                else:
                    break
            if elegir_top == 1:
                df = df.reset_index(drop=True)
                df.index = df.index + 1
                df.drop(df.index[10:6000], inplace=True)
                clear.clear()
                print(linea_separadora * 2, salto, "Top 10",salto, linea_separadora * 2)
                print(tabulate(df, tablefmt = 'fancy_grid', headers = [columna_elegida, segunda_columna_elegida, "Forma de medida", "cantidad por millon"]))
            elif elegir_top == 2:
                df = df.reset_index(drop=True)
                df.index = df.index + 1
                df.drop(df.index[50:6000], inplace=True)
                clear.clear()
                print(linea_separadora * 2, salto, "Top 50",salto, linea_separadora * 2)
                print(tabulate(df, tablefmt = 'fancy_grid', headers = [columna_elegida, segunda_columna_elegida, "Forma de medida", "cantidad por millon"]))
            else:
                df = df.reset_index(drop=True)
                df.index = df.index + 1
                df.drop(df.index[100:6000], inplace=True)
                clear.clear()
                print(linea_separadora * 2, salto, "Top 100",salto, linea_separadora * 2)
                print(tabulate(df, tablefmt = 'fancy_grid', headers = [columna_elegida, segunda_columna_elegida, "Forma de medida", "cantidad por millon"]))    
    except:
        print(linea_separadora * 2, salto, "No se puede mostrar la tabla de la forma pedida, por ende se mostrara de forma normal", salto, linea_separadora * 2)
        print(tabulate(df, showindex = False, tablefmt = 'fancy_grid'))
    return df

def crear_elegir_archivo_guardar_datos_csv(columna_elegida, segunda_columna_elegida, dato_elegido, segundo_dato_elegido, tabla):
    """Esta funcion crea un archivo csv el cual puede nombrar el usuario, tambien utiliza listdir para enlistar los archivos disponibles
    y mkdir para crear una carpeta"""
    linea_separadora = "-" * 65
    salto = "\n"
    print(linea_separadora * 2, salto, "Desea crear un archivo para guardar los datos elegidas junto a la tabla mostrada? S/N ", salto, linea_separadora * 2)
    pregunta = input().upper().strip()
    if not pregunta or pregunta == "N":
        print(linea_separadora * 2, salto, "Muchas gracias", salto, linea_separadora * 2)
        return
    else:
        clear.clear()
        try:
            mkdir(str(ruta_general) + "/Trabajo_final/guardar_datos_tablas")
        except:
            pass
        while True:
            print(linea_separadora * 2, salto, "Desea ver los archivos ya creados? S/N: ", salto, linea_separadora * 2)
            elegir = input().strip().upper()
            if not elegir or elegir == "N":
                while True:
                    print(linea_separadora * 2)
                    nombre_archivo = input("Por favor escriba el nombre que va poseer el archivo: ").strip()
                    print(linea_separadora * 2)
                    if not nombre_archivo:
                        print(linea_separadora * 2, salto, "Por favor ingrese un nombre para el archivo", salto, linea_separadora * 2)
                        input("Precione <Enter> para continuar")
                        clear.clear()
                        continue
                    else:
                        break
                break
            else:
                listar_archivos = listdir("Trabajo_final/guardar_datos_tablas")
                if len(listar_archivos) != 0:
                    while True:
                        clear.clear() 
                        muestra = []
                        archivos_disponibles = {}
                        indice = 1
                        for archivos in listar_archivos:
                            archivos_disponibles[indice] = archivos[:-4]
                            muestra.append(str(indice) + ":" +  " " + archivos)
                            indice += 1
                        print(linea_separadora * 2)
                        print(tabulate(muestra, tablefmt = 'fancy_grid'), salto, linea_separadora * 2)
                        print(linea_separadora * 2, salto, "Por favor elija el numero del archivo: ", salto, linea_separadora * 2)
                        archivo_elegido = input().strip()
                        try:
                            archivo_elegido = int(archivo_elegido)
                        except:
                            print(linea_separadora * 2, salto, "Por favor ingrese uno de los archivos: ")
                            input("Precione <ENTER>")
                            print(linea_separadora * 2)
                            continue  
                        if not archivo_elegido in archivos_disponibles or not archivo_elegido:
                            print(linea_separadora * 2, salto, "Por favor ingrese uno de los archivos: ")
                            input("Precione <ENTER>")
                            print(linea_separadora * 2)
                            continue
                        else:
                            nombre_archivo = archivos_disponibles[archivo_elegido]
                            break
                    break
                else:
                    print(linea_separadora * 2, salto, "No hay archivos para elegir, por favor cree uno")
                    input("Precione <ENTER>")
                    print(linea_separadora * 2)
                    clear.clear()
                    continue
    return nombre_archivo

def guardar_datos_csv(columna_elegida, segunda_columna_elegida, dato_elegido, segundo_dato_elegido, tabla, nombre_archivo):
    """Esta funcion permite guardar los datos elegidos durante el programa y con la libreria pandas se exporta el Dataframe a un archivo csv"""
    guardar_datos = open("Trabajo_final/guardar_datos_tablas/" + nombre_archivo + ".csv", "a")
    guardar_datos.writelines(salto)
    if segunda_columna_elegida == None:
        guardar_datos.writelines(linea_separadora + linea_separadora + salto)
        guardar_datos.writelines("La columna elegida fue:" + salto)
        guardar_datos.writelines(columna_elegida + salto)
        guardar_datos.writelines("El dato elegido fue:" + salto)
        guardar_datos.writelines(str(dato_elegido) + salto)
    else:
        guardar_datos.writelines(linea_separadora + linea_separadora + salto)
        guardar_datos.writelines("Las columnas elegidas fueron:" + salto)
        guardar_datos.writelines("Primera columna: " + " " + columna_elegida + salto)
        guardar_datos.writelines("Segunda columna: " + " " + segunda_columna_elegida + salto)
        guardar_datos.writelines("Los daotos elegidos fueron:" + salto)
        guardar_datos.writelines("Primer dato: " + " " + str(dato_elegido) + salto)
        guardar_datos.writelines("Segundo dato: " + " " + str(segundo_dato_elegido) + salto)
    guardar_datos.writelines("La tabla mostrada fue: " + salto)
    guardar_datos.writelines(linea_separadora + linea_separadora + salto)
    guardar_datos.close()
    tabla.to_csv("Trabajo_final/guardar_datos_tablas/" + nombre_archivo + ".csv", mode = "a", index = False)
    return

#Cuerpo principal
linea_separadora = "-" * 65
salto = "\n"
ruta_general = getcwd()
try:
    mkdir(str(ruta_general) + "/Trabajo_final")
except:
    pass
ruta_1983_2016 = crear_archivo()
clear.clear()
print(linea_separadora * 2, salto, "Bienvenido, este programa trata de filtrar datos productos lactios de leche cruda a su producto destino", salto, linea_separadora * 2)
input("Precione enter para iniciar el programa")
while True:
    clear.clear()
    columna_elegida = elegir_columna()
    cuarto_archivo = str(ruta_general) + "/Trabajo_final/destino-produccion-leche-1983-2016.csv"
    print(linea_separadora * 2)
    preguntar_segunda_columna = input("desea elegir otra columna? S o N ").strip().upper()
    print(linea_separadora * 2)
    if not preguntar_segunda_columna or preguntar_segunda_columna == "N":
        while True:
            opciones_primer_dato, muestra = procesar_primera_columna_elegida_mostrar_opciones(cuarto_archivo, columna_elegida)
            dato_elegido = elegir_primer_dato(columna_elegida, opciones_primer_dato, muestra)
            datos_procesados = procesar_archivo_por_un_dato(cuarto_archivo, columna_elegida, dato_elegido)
            tabla = crear_mostrar_tabla_extensa(datos_procesados)
            segunda_columna_elegida = None
            segundo_dato_elegido = None
            nombre_archivo = crear_elegir_archivo_guardar_datos_csv(columna_elegida, segunda_columna_elegida, dato_elegido, segundo_dato_elegido, tabla)
            if nombre_archivo == None:
                break
            else:
                guardar_datos_csv(columna_elegida, segunda_columna_elegida, dato_elegido, segundo_dato_elegido, tabla, nombre_archivo)
            break
    else:
      while True:
        clear.clear()
        print(linea_separadora * 2, salto, "Primera columna: ", columna_elegida, salto, linea_separadora * 2)
        segunda_columna_elegida = elegir_columna()
        if columna_elegida == segunda_columna_elegida:
            print(linea_separadora * 2, salto, "No puedes elegir 2 veces el mismo dato, por favor elija otro", salto, linea_separadora * 2)
            input("Precione enter para continuar")
            continue
        else:
            while True:
                opciones_primer_dato, muestra = procesar_primera_columna_elegida_mostrar_opciones(cuarto_archivo, columna_elegida)    
                dato_elegido = elegir_primer_dato(columna_elegida, opciones_primer_dato, muestra)
                opciones_segundo_dato, muestra = procesar_segunda_columna_elegida_mostrar_opciones(cuarto_archivo, dato_elegido, segunda_columna_elegida)
                segundo_dato_elegido = elegir_segundo_dato(segunda_columna_elegida, opciones_segundo_dato, muestra)
                break
            datos_procesados = procesar_archivo_por_dos_datos(cuarto_archivo, columna_elegida, segunda_columna_elegida, dato_elegido, segundo_dato_elegido)
            tabla = crear_mostrar_tabla_corta(datos_procesados, columna_elegida, segunda_columna_elegida)
            nombre_archivo = crear_elegir_archivo_guardar_datos_csv(columna_elegida, segunda_columna_elegida, dato_elegido, segundo_dato_elegido, tabla)
            if nombre_archivo == None:
                break
            else:
                guardar_datos_csv(columna_elegida, segunda_columna_elegida, dato_elegido, segundo_dato_elegido, tabla, nombre_archivo)
            break
    clear.clear()
    print(linea_separadora * 2, salto, "Quieres volver al inicio?  S o N: ", salto, linea_separadora * 2)
    pregunta = input().upper().strip()
    if pregunta == "N" or not pregunta:
        print("Muchas gracias por tu tiempo")
        clear.clear()
        exit()
    else:
        continue