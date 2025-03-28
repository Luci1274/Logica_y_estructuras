#Importaciones
from os import getcwd, listdir, mkdir
import clear
import pandas as pd
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

def elegir_columna():
    """Esta funcion nos permite elegir la columna por la cual deseamos realizar filtrado"""
    linea_separadora = "-" * 65
    separador = "\n"
    columnas_disponibles = {1:"año",2:"mes",3:"producto destino",4:"cantidad por millón"}
    muestra = [[1, "año"], [2, "mes"], [3, "producto destino"], [4, "cantidad por millón"], [0, "Aprete para salir"]]
    while True:
        print(tabulate(muestra, tablefmt = 'fancy_grid'))
        try:
            print(linea_separadora)
            eleccion = input(separador + "Por favor elija la columna que más le guste o aprete <0> para salir: ").strip()
            print(linea_separadora)
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

def procesar_primera_columna_elegida_mostrar_opciones(cuarto_archivo, columna_elegida):
    clear.clear()
    linea_separadora = "-" * 65
    salto = "\n"
    muestra = []
    archivo = open(cuarto_archivo, "r").readlines()
    print(linea_separadora, salto, "Ahora elegirá de forma más especifica el/la", columna_elegida, salto, linea_separadora)
    while True:
        if columna_elegida == "año":
            opciones_primer_dato = set({})
            for años in archivo:
                separador = años.split(",")
                opciones_primer_dato.add(separador[2])
            opciones_primer_dato.remove("año")
            for mostrar_años in opciones_primer_dato:
                muestra.append(mostrar_años + salto)
            muestra.sort()
            print(salto, tabulate(muestra, tablefmt = "grid"), salto)
            return opciones_primer_dato, muestra
        elif columna_elegida == "mes":
            opciones_primer_dato = set({})
            for meses in archivo:
                separador = meses.split(",")
                opciones_primer_dato.add(separador[3])
            opciones_primer_dato.remove("mes")
            for Mostrar_meses in range(1, 13):
                muestra.append(str(Mostrar_meses))
                muestra.append(salto)
            print(salto, tabulate(muestra, tablefmt = "grid"))
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
                muestra.append(str(indice) + ":" +  " " + productos_disponibles + salto)
                indice += 1
            print(salto, tabulate(muestra, tablefmt = "grid"))
            return opciones_primer_dato, muestra
        elif columna_elegida == "cantidad por millón":
            conjunto_cantidad_millon = set({})
            for cantidad_millon in archivo:
                separador = cantidad_millon.split(",")
                conjunto_cantidad_millon.add(separador[10])
            indice = 1
            opciones_primer_dato = {}
            pausa = [518, 1036, 1554, 2072, 2590, 3108, 3626, 3975, 4493]
            for millon_disponible in conjunto_cantidad_millon:
                opciones_primer_dato[indice] = millon_disponible
                muestra.append(str(indice) + ":" +  " " + millon_disponible)
                indice += 1
                if indice in pausa:
                    print(salto,tabulate(muestra, tablefmt = "grid"), salto)
                    corte = input("Presione <ENTER> para ver las demás opciones o precione 0 para saltar la muestra: ").strip()
                    clear.clear()
                    if corte == "0":
                        muestra.clear()
                        opciones_primer_dato.clear()
                        indice = 1
                        for millon_disponible in conjunto_cantidad_millon:
                            opciones_primer_dato[indice] = millon_disponible
                            muestra.append(str(indice) + ":" +  " " + millon_disponible)
                            indice += 1
                        return opciones_primer_dato, muestra 
                    else:
                        clear.clear()
            return opciones_primer_dato, muestra

def elegir_primer_dato(columna_elegida, opciones_primer_dato, muestra):
    """En esta funcion elegiremos el dato que fue recopilado en las anteriores funciones
    debiendo escribir la palabra o numero que deseamos"""
    linea_separadora = "-" * 65
    salto = "\n"
    while True:
        if columna_elegida == "año":
            ingresar = input("Por favor ingrese un año 1983 en adelante: ").strip()
            try:
                int(ingresar)
            except:
                print(linea_separadora, salto, "Por favor ingrese un año valido", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                print(salto,tabulate(muestra, tablefmt = "grid"), salto)
                continue
            if not ingresar:
                print(linea_separadora, salto, "Por favor ingrese un año ", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                print(salto,tabulate(muestra, tablefmt = "grid"), salto, linea_separadora)
                continue
            elif not ingresar in opciones_primer_dato:
                print(linea_separadora, salto, "Por favor elija uno de los siguientes años ", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                print(salto,tabulate(muestra, tablefmt = "grid"), salto)
                continue
            else:
                dato_elegido = ingresar
                return dato_elegido        
        elif columna_elegida == "mes":
            ingresar = input("Por favor ingrese uno de estos meses: ")
            try:
                int(ingresar)
            except:
                print(linea_separadora, salto, "Por favor ingrese uno de los meses mostrados", salto, linea_separadora)
                input("Presione <ENTER>")
                print(linea_separadora)
                continue
            if not ingresar or not ingresar in opciones_primer_dato:
                print(linea_separadora, salto, "Por favor ingrese un mes de los antes mostrados: ", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                print(salto,tabulate(muestra, tablefmt = "grid"), salto)
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
                print(linea_separadora, salto, "Por favor el numero del producto", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                print(salto,tabulate(muestra, tablefmt = "grid"), salto)
                continue
            if not ingresar:
                print(linea_separadora, salto, "Por favor ingrese un producto: ", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                print(salto,tabulate(muestra, tablefmt = "grid"), salto)
                continue
            elif not ingresar in opciones_primer_dato:
                print(linea_separadora, salto, "Por favor elija uno de los siguientes productos: ", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                print(salto,tabulate(muestra, tablefmt = "grid"), salto)
                continue
            else:
                dato_elegido = opciones_primer_dato[ingresar]
                return dato_elegido
        elif columna_elegida == "cantidad por millón":
            volver_mostrar_muestra = []
            print(linea_separadora, salto, "Por favor ingrese un numero del 1 hasta el", len(muestra), ": " , salto, linea_separadora)
            ingresar = input()
            try:
                ingresar = int(ingresar)
            except:
                clear.clear()
                print(linea_separadora, salto, "Por favor ingrese el numero de la cantidad", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                pausa = [518, 1036, 1554, 2072,2590, 3108, 3626, 3975, 4493]
                indice = 1
                for millon_disponible in muestra:
                    volver_mostrar_muestra.append(str(indice) + ":" +  " " + millon_disponible)
                    indice += 1
                    if indice in pausa:
                        print(salto,tabulate(volver_mostrar_muestra, tablefmt = "grid"), salto, linea_separadora)
                        corte = input("Presione <ENTER> para ver las demás opciones o precione 0 para saltar la muestra: ").strip()
                        clear.clear()
                        if corte == "0":
                            clear.clear()
                            break
                continue
            if not ingresar:
                print(linea_separadora, salto, "Por favor ingrese una cantidad: ", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                pausa = [518, 1036, 1554, 2072, 2590, 3108, 3626, 3975, 4493]
                indice = 1
                for millon_disponible in muestra:
                    volver_mostrar_muestra.append(str(indice) + ":" +  " " + millon_disponible)
                    indice += 1
                    if indice in pausa:
                        print(salto,tabulate(volver_mostrar_muestra, tablefmt = "grid"), salto, linea_separadora)
                        corte = input("Presione <ENTER> para ver las demás opciones o precione 0 para saltar la muestra: ")
                        clear.clear()
                        if corte == "0":
                            break
                continue
            elif not ingresar in opciones_primer_dato:
                print(linea_separadora, salto, "Por favor elija uno de las siguientes cantidades: ", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                pausa = [518, 1036, 1554, 2072, 2590, 3108, 3626, 3975, 4493]
                indice = 1
                for millon_disponible in muestra:
                    volver_mostrar_muestra.append(str(indice) + ":" +  " " + millon_disponible)
                    indice += 1
                    if indice in pausa:
                        print(salto,tabulate(volver_mostrar_muestra, tablefmt = "grid"), salto, linea_separadora)
                        corte = input("Presione <ENTER> para ver las demás opciones o precione 0 para salta la muestra: ")
                        clear.clear()
                        if corte == "0":
                            break
                continue
            else:
                dato_elegido = opciones_primer_dato[ingresar]
                return dato_elegido

def procesar_segunda_columna_elegida_mostrar_opciones(cuarto_archivo, dato_elegido, segunda_columna_elegida):
    clear.clear()
    linea_separadora = "-" * 65
    salto = "\n"
    muestra = []
    archivo = open(cuarto_archivo, "r").readlines()
    print(linea_separadora, salto, "Ahora elegirá de forma más especifica el/la", segunda_columna_elegida, salto, linea_separadora)
    while True:
        if segunda_columna_elegida == "año":
            opciones_segundo_dato = set({})
            for años in archivo:
                if dato_elegido in años:
                    separador = años.split(",")
                    opciones_segundo_dato.add(separador[2])
            try:
                opciones_segundo_dato.remove("año")
            except:
                pass
            for mostrar_años in opciones_segundo_dato:
                muestra.append(mostrar_años + salto)
            muestra.sort()
            print(salto, tabulate(muestra, tablefmt = "psql"), salto)
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
            for Mostrar_meses in opciones_segundo_dato:
                muestra.append(Mostrar_meses + salto)
            muestra.sort()
            print(salto, tabulate(muestra, tablefmt = "psql"))
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
                muestra.append(str(indice) + ":" +  " " + productos_disponibles + salto)
                indice += 1
            print(salto, tabulate(muestra, tablefmt = "psql"))
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
            pausa = [1 , 2, 3, 4, 5, 6, 15, 20, 518, 1036, 1554, 2072, 2590, 3108, 3626, 3975, 4493]
            for millon_disponible in conjunto_cantidad_millon:
                opciones_segundo_dato[indice] = millon_disponible
                muestra.append(str(indice) + ":" +  " " + millon_disponible)
                indice += 1
                if indice in pausa:
                    print(salto,tabulate(muestra, tablefmt = "psql"), salto)
                    corte = input("Presione <ENTER> para ver las demás opciones o precione 0 para saltar la muestra ")
                    clear.clear()
                    if corte == "0":
                        clear.clear()
                        opciones_segundo_dato.clear()
                        muestra.clear()
                        indice = 1
                        for millon_disponible in conjunto_cantidad_millon:
                            opciones_segundo_dato[indice] = millon_disponible
                            muestra.append(str(indice) + ":" +  " " + millon_disponible)
                            indice += 1
                        return opciones_segundo_dato, muestra
            return opciones_segundo_dato, muestra

def elegir_segundo_dato(segunda_columna_elegida, opciones_segundo_dato, muestra):
    """Esta funcion recopila datos que estén relacionados con el primer dato que elegimos 
    y además nos permite elegir un dato especifico para filtrar"""
    linea_separadora = "-" * 65
    salto = "\n"
    while True:
        if segunda_columna_elegida == "año":
            ingresar = input("Por favor ingrese uno de estos años: ").strip()
            try:
                int(ingresar)
            except:
                print(linea_separadora, salto, "Por favor ingrese un año valido", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                print(salto,tabulate(muestra, tablefmt = "psql"), salto)
                continue
            if not ingresar:
                print(linea_separadora, salto, "Por favor ingrese un año ", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                print(salto,tabulate(muestra, tablefmt = "psql"), salto, linea_separadora)
                continue
            elif not ingresar in opciones_segundo_dato:
                print(linea_separadora, salto, "Por favor elija uno de los siguientes años ", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                print(salto,tabulate(muestra, tablefmt = "psql"), salto)
                continue
            else:
                segundo_dato_elegido = ingresar
                return segundo_dato_elegido        
        elif segunda_columna_elegida == "mes":
            ingresar = input("Por favor ingrese uno de estos meses: ")
            try:
                int(ingresar)
            except:
                print(linea_separadora, salto, "Por favor ingrese uno de los meses mostrados", salto, linea_separadora)
                input("Presione <ENTER>")
                input("Presione <ENTER>")
                clear.clear()
                print(salto,tabulate(muestra, tablefmt = "psql"), salto)
                continue
            if not ingresar or not ingresar in opciones_segundo_dato:
                print(linea_separadora, salto, "Por favor ingrese un mes de los antes mostrados: ", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                print(salto,tabulate(muestra, tablefmt = "psql"), salto)
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
                print(linea_separadora, salto, "Por favor el numero del producto", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                print(salto,tabulate(muestra, tablefmt = "psql"), salto)
                continue
            if not ingresar:
                print(linea_separadora, salto, "Por favor ingrese un producto: ", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                print(salto,tabulate(muestra, tablefmt = "psql"), salto)
                continue
            elif not ingresar in opciones_segundo_dato:
                print(linea_separadora, salto, "Por favor elija uno de los siguientes productos: ", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                print(salto,tabulate(muestra, tablefmt = "psql"), salto)
                continue
            else:
                segundo_dato_elegido = opciones_segundo_dato[ingresar]
                return segundo_dato_elegido
        elif segunda_columna_elegida == "cantidad por millón":
            print(linea_separadora, salto, "Por favor ingrese un numero del 1 hasta el", len(muestra), ": ")
            volver_mostrar_muestra = []
            ingresar = input()
            try:
                ingresar = int(ingresar)
            except:
                clear.clear()
                print(linea_separadora, salto, "Por favor ingrese el numero de la cantidad", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                pausa = [1 , 2, 3, 4, 5, 6, 15, 20, 518, 1036, 1554, 2072, 2590, 3108, 3626, 3975, 4493]
                indice = 1
                for millon_disponible in muestra:
                    volver_mostrar_muestra.append(str(indice) + ":" +  " " + millon_disponible)
                    indice += 1
                    if indice in pausa:
                        print(salto,tabulate(volver_mostrar_muestra, tablefmt = "psql"), salto, linea_separadora)
                        corte = input("Presione <ENTER> para ver las demás opciones o precione 0 para saltar la muestra").strip()
                        clear.clear()
                        if corte == "0":
                            break
                continue
            if not ingresar:
                print(linea_separadora, salto, "Por favor ingrese una cantidad: ", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                pausa = [1 , 2, 3, 4, 5, 6, 15, 20, 518, 1036, 1554, 2072, 2590, 3108, 3626, 3975, 4493]
                indice = 1
                for millon_disponible in muestra:
                    volver_mostrar_muestra.append(str(indice) + ":" +  " " + millon_disponible)
                    indice += 1
                    if indice in pausa:
                        print(salto,tabulate(volver_mostrar_muestra, tablefmt = "psql"), salto, linea_separadora)
                        corte = input("Presione <ENTER> para ver las demás opciones o precione 0 para salta la muestra").strip()
                        clear.clear()
                        if corte == "0":
                            break
                continue
            elif not ingresar in opciones_segundo_dato:
                print(linea_separadora, salto, "Por favor elija uno de las siguientes cantidades: ", salto, linea_separadora)
                input("Presione <ENTER>")
                clear.clear()
                pausa = [1 , 2, 3, 4, 5, 6, 15, 20, 518, 1036, 1554, 2072, 2590, 3108, 3626, 3975, 4493]
                indice = 1
                for millon_disponible in muestra:
                    volver_mostrar_muestra.append(str(indice) + ":" +  " " + millon_disponible)
                    indice += 1
                    if indice in pausa:
                        print(salto,tabulate(volver_mostrar_muestra, tablefmt = "grid"), salto, linea_separadora)
                        corte = input("Presione <ENTER> para ver las demás opciones o precione 0 para saltar la muestra").strip()
                        clear.clear()
                        if corte == "0":
                            break
                continue
            else:
                segundo_dato_elegido = opciones_segundo_dato[ingresar]
                return segundo_dato_elegido

def procesar_archivo__por_un_dato(cuarto_archivo, columna_elegida, dato_elegido):
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
    """Esta funcion recopila datos relacionados a la eleccion y devuelve un diccionario"""
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
    """Esta funcion nos permite visualizar una tabla además de otras opciones"""
    linea_separadora = "-" * 65
    salto = "\n"
    clear.clear()
    df = pd.DataFrame(datos_procesados)
    try:    
        print(linea_separadora)
        ascendente = input("Desea verlo de forma ascendente? S o N: ")
        print(linea_separadora)
        if not ascendente or ascendente == "N":
            df = df.sort_values("cantidad millon", ascending = False)    
        else:
            df = df.sort_values("cantidad millon", ascending = True)
        print(linea_separadora)
        top = input("Desea verlo en un top? s o n: ").upper().strip()
        print(linea_separadora)
        if not top or top == "N":
            clear.clear()
            print(salto, tabulate(df, showindex = False, tablefmt = 'fancy_grid', headers = ["años", "meses", "producto destino", "unidad med.", "cantidad por millon"]), salto)
        else:
            while True:
                tops_disponibles = {1: 10, 2: 50, 3: 100}
                print(salto, linea_separadora, salto, "1", tops_disponibles[1], salto, "2", tops_disponibles[2], salto, "3", tops_disponibles[3], salto, linea_separadora)
                elegir_top = input("Ingrese el numero del top que desee ver: ")
                print(linea_separadora)
                try:
                    elegir_top = int(elegir_top)
                except:
                    clear.clear()
                    print(linea_separadora, salto,"Por favor elija uno de los numeros de adelante", salto, linea_separadora)
                    continue
                if not elegir_top or not elegir_top in tops_disponibles:
                    print(linea_separadora, salto, "Por favor elija uno de los numeros de adelante", salto, linea_separadora)
                    continue
                else:
                    break
            if elegir_top == 1:
                df = df.reset_index(drop = True)
                df.index = df.index + 1
                df.drop(df.index[10:6000], inplace = True)
                clear.clear()
                print(linea_separadora, salto, "Top 10",salto, linea_separadora, salto, tabulate(df, tablefmt = 'fancy_grid', headers = ["años", "meses", "producto destino", "unidad med.", "cantidad por millon"]), salto)
            elif elegir_top == 2:
                df = df.reset_index(drop = True)
                df.index = df.index + 1
                df.drop(df.index[50:6000], inplace = True)
                clear.clear()
                print(linea_separadora, salto, "Top 50",salto, linea_separadora, salto, tabulate(df, tablefmt = 'fancy_grid', headers = ["años", "meses", "producto destino", "unidad med.", "cantidad por millon"]), salto)
            else:
                df = df.reset_index(drop = True)
                df.index = df.index + 1
                df.drop(df.index[100:6000], inplace = True)
                clear()
                print(linea_separadora, salto, "Top 100",salto, linea_separadora, salto, tabulate(df, tablefmt = 'fancy_grid', headers = ["años", "meses", "producto destino", "unidad med.", "cantidad por millon"]), salto)    
        print(linea_separadora)
        pausa = input("Precione <ENTER> para continuar")
        print(linea_separadora)
    except:
        print(linea_separadora, salto, "No se puede mostrar la tabla de la forma pedida, por ende se mostrara de forma normal", salto, linea_separadora)
        print(tabulate(df, showindex = False, tablefmt = 'fancy_grid', headers = ["años", "meses", "producto destino", "unidad med.", "cantidad por millon"]))
    return df

def crear_mostrar_tabla_corta(datos_procesados, columna_elegida, segunda_columna_elegida):
    """Esta funcion nos permite visualizar una tabla además de otras opciones"""
    clear.clear()
    linea_separadora = "-" * 65
    salto = "\n"
    datos_procesados
    df = pd.DataFrame(datos_procesados)
    try:
        if columna_elegida != "cantidad por millón" and segunda_columna_elegida != "cantidad por millón":
            print(linea_separadora)
            ascendente = input("Desea verlo de forma ascendente? S o N: ")
            print(linea_separadora)
            if not ascendente or ascendente == "N":
                df = df.sort_values( "cantidad millon", ascending = False)    
            else:
                df = df.sort_values("Cantidad millon", ascending = True)
                print(linea_separadora)
        else:
            clear.clear()
            print(salto, tabulate(df, showindex = False, tablefmt = 'fancy_grid'), salto)
            print(linea_separadora)
            pausa = input("Precione <ENTER> para continuar")
            print(linea_separadora)
            return df

        top = input("Desea verlo en un top? s o n: ").upper().strip()
        print(linea_separadora)
        if not top or top == "N":
            print(salto, tabulate(df, showindex = False, tablefmt = 'fancy_grid'), salto)
        else:
            while True:
                tops_disponibles = {1: 10, 2: 50, 3: 100}
                print(salto, linea_separadora, salto, "1", tops_disponibles[1], salto, "2", tops_disponibles[2], salto, "3", tops_disponibles[3], salto, linea_separadora)
                elegir_top = input("Ingrese el numero del top que desee ver: ")
                print(linea_separadora)
                try:
                    elegir_top = int(elegir_top)
                except:
                    clear.clear()
                    print(salto, linea_separadora, "Por favor elija uno de los numeros de adelante", salto, linea_separadora)
                    continue
                if not elegir_top or not elegir_top in tops_disponibles:
                    print(salto, linea_separadora, "Por favor elija uno de los numeros de adelante", salto, linea_separadora)
                    continue
                else:
                    break
            if elegir_top == 1:
                df = df.reset_index(drop=True)
                df.index = df.index + 1
                df.drop(df.index[10:6000], inplace=True)
                clear.clear()
                print(linea_separadora, salto, "Top 10",salto, linea_separadora, salto, tabulate(df, tablefmt = 'fancy_grid'), salto)
            elif elegir_top == 2:
                df = df.reset_index(drop=True)
                df.index = df.index + 1
                df.drop(df.index[50:6000], inplace=True)
                clear.clear()
                print(linea_separadora, salto, "Top 50",salto, linea_separadora, salto, tabulate(df, tablefmt = 'fancy_grid'), salto)
            else:
                df = df.reset_index(drop=True)
                df.index = df.index + 1
                df.drop(df.index[100:6000], inplace=True)
                clear.clear()
                print(linea_separadora, salto, "Top 100",salto, linea_separadora, salto, tabulate(df, tablefmt = 'fancy_grid'), salto)    
    except:
        print(linea_separadora, salto, "No se puede mostrar la tabla de la forma pedida, por ende se mostrara de forma normal", salto, linea_separadora)
        print(tabulate(df, showindex = False, tablefmt = 'fancy_grid'))
    return df

def crear_elegir_archivo_guardar_datos(columna_elegida, segunda_columna_elegida, dato_elegido, segundo_dato_elegido, tabla):
    """"""
    linea_separadora = "-" * 65
    salto = "\n"
    print(linea_separadora, salto, "Desea crear un archivo para guardar los datos elegidas junto a la tabla mostrada? S/N ", salto, linea_separadora)
    pregunta = input().upper().strip()
    if not pregunta or pregunta == "N":
        print(linea_separadora, salto, "Muchas gracias", salto, linea_separadora)
        return
    else:
        clear.clear()
        try:
            mkdir(str(ruta_general) + "/Trabajo_final/guardar_datos_tablas")
        except:
            pass
        while True:
            print(linea_separadora, salto, "Desea ver los archivos ya creados? S/N: ", salto, linea_separadora)
            elegir = input().strip().upper()
            if not elegir or elegir == "N":
                while True:
                    print(linea_separadora)
                    nombre_archivo = input("Por favor escriba el nombre que va poseer el archivo: ").strip()
                    print(linea_separadora)
                    if not nombre_archivo:
                        print(linea_separadora, salto, "Por favor ingrese un nombre para el archivo", salto, linea_separadora)
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
                        print(linea_separadora, salto, tabulate(muestra, tablefmt = 'fancy_grid'), salto, linea_separadora)
                        print(linea_separadora, salto, "Por favor elija el numero del archivo: ", salto, linea_separadora)
                        archivo_elegido = input().strip()
                        try:
                            archivo_elegido = int(archivo_elegido)
                        except:
                            print(linea_separadora, salto, "Por favor ingrese uno de los archivos: ")
                            input("Precione <ENTER>")
                            print(linea_separadora)
                            continue  
                        if not archivo_elegido in archivos_disponibles or not archivo_elegido:
                            print(linea_separadora, salto, "Por favor ingrese uno de los archivos: ")
                            input("Precione <ENTER>")
                            print(linea_separadora)
                            continue
                        else:
                            nombre_archivo = archivos_disponibles[archivo_elegido]
                            break
                    break
                else:
                    print(linea_separadora, salto, "No hay archivos para elegir, por favor cree uno")
                    input("Precione <ENTER>")
                    print(linea_separadora)
                    clear.clear()
                    continue
        guardar_datos = open("Trabajo_final/guardar_datos_tablas/" + nombre_archivo + ".csv", "a")
        guardar_datos.write(linea_separadora + linea_separadora + salto)
        guardar_datos.write("Columna escogida: " + columna_elegida + salto)
        guardar_datos.write("Dato escogido: " + str(dato_elegido) + salto)
        if segunda_columna_elegida == None:
            pass
        else:
            guardar_datos.write("Segunda columna escogida: " + segunda_columna_elegida + salto)
            guardar_datos.write("Segundo dato escogido: " + str(segundo_dato_elegido) + salto)
        guardar_datos.write(linea_separadora + linea_separadora + salto)
        tabla.to_csv("Trabajo_final/guardar_datos_tablas/" + nombre_archivo + ".csv", mode = "a", index = False)
    guardar_datos.close()
    return

#Cuerpo principal
linea_separadora = "-" * 65
salto = "\n"
ruta_general = getcwd()
try:
    mkdir(str(ruta_general) + "/Trabajo_final")
except:
    pass
ruta_1988 = str(ruta_general) + "/Trabajo_final/destino-produccion-leche-1983-1988.csv"
ruta_2007 = str(ruta_general) + "/Trabajo_final/destino-produccion-leche-1989-2007.csv"
ruta_2016 = str(ruta_general) + "/Trabajo_final/destino-produccion-leche-2008-2016.csv"
ruta_1983_2016 = crear_archivo(ruta_1988, ruta_2007, ruta_2016)
clear.clear()
print(linea_separadora, salto, "Bienvenido, este programa trata de filtrar datos productos lacteos", salto, linea_separadora)
input("Precione enter para iniciar el programa")
while True:
    clear.clear()
    columna_elegida = elegir_columna()
    cuarto_archivo = str(ruta_general) + "/Trabajo_final/destino-produccion-leche-1983-2016.csv"
    print(linea_separadora)
    preguntar_segunda_columna = input("desea elegir otra columna? S o N ").strip().upper()
    print(linea_separadora)
    if not preguntar_segunda_columna or preguntar_segunda_columna == "N":
        while True:
            opciones_primer_dato, muestra = procesar_primera_columna_elegida_mostrar_opciones(cuarto_archivo, columna_elegida)
            dato_elegido = elegir_primer_dato(columna_elegida, opciones_primer_dato, muestra)
            datos_procesados = procesar_archivo__por_un_dato(cuarto_archivo, columna_elegida, dato_elegido)
            tabla = crear_mostrar_tabla_extensa(datos_procesados)
            segunda_columna_elegida = None
            segundo_dato_elegido = None
            crear_elegir_archivo_guardar_datos(columna_elegida, segunda_columna_elegida, dato_elegido, segundo_dato_elegido, tabla)
            break
    else:
      while True:
        segunda_columna_elegida = elegir_columna()
        if columna_elegida == segunda_columna_elegida:
            print("No puedes elegir 2 veces el mismo dato, por favor elija otro")
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
            crear_elegir_archivo_guardar_datos(columna_elegida, segunda_columna_elegida, dato_elegido, segundo_dato_elegido, tabla)
            break
    print(linea_separadora, salto, "Quieres volver al inicio?  S o N: ", salto, linea_separadora)
    pregunta = input().upper().strip()
    if pregunta == "N" or not pregunta:
        print("Muchas gracias por tu tiempo")
        clear.clear()
        exit()
    else:
        continue