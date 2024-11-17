def crear_archivo(ruta_de_archivo):
    """La función crea y cierra un archivo de texto"""    
    try:
        crear_archivo_personas = open(ruta_de_archivo, "x")
        crear_archivo_personas.close()
    except:
        print("El archivo ya fue creado")
    return

def buscar_palabras(leer_archivo,palabras,largo_maximo):
    """Busca el total,minimo,maximo y el promedio de palabras"""
    largo_maximo
    while True:
        lectura = leer_archivo.readlines()
        if not lectura:
           break
        for letras in lectura:
            palabras.append(len(letras))
    leer_archivo.close()        
    return palabras
ruta_de_archivo = "/home/luci/Documentos/python/logica/palabras/spanish.lst"
crear_archivo(ruta_de_archivo)
palabras = []
leer_archivo = open(ruta_de_archivo,"r")
largo_minimo = 1
largo_maximo = 0
largo_promedio = 0
largo_maximo = buscar_palabras(leer_archivo,palabras,largo_maximo)
print(largo_maximo)