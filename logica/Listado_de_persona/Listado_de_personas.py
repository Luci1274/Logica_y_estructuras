def crear_archivo(ruta_archivo):
    """La función crea y cierra un archivo de texto"""    
    try:
        crear_archivo_personas = open(ruta_archivo, "x")
        crear_archivo_personas.close()
    except:
        print("El archivo ya fue creado")
    return

def lectura_del_archivo(personas_modo_lectura, personas):
    """ lectura secuencial del archivo y carga en lista personas, quitandole el enter al final de cada uno """
    while True:
        persona = personas_modo_lectura.readline()
        if not persona:
            break
        personas.append(persona[:-1])
    personas_modo_lectura.close()
    return personas

def validaciones_varias(ingresos_validos, ingresos_invalidos, persona, personas):
    """validaciones varias: solo texto, 2 o mas palabras y no repetido"""    
    ok = True
    for caracter in persona:
        if caracter.isdigit():
            ok = False
            resultado = print('Solo se permiten letras')
            
    if len(persona.split()) == 1:
        ok = False
        resultado = print('Debería ingresar Apellido y Nombre/s')

    if persona in personas:
        ok = False
        resultado = print('El persona ya fue ingresado')        
    
    if ok == True:
        resultado = print("")

    if ok:
        personas.append(persona)
        ingresos_validos += 1
    else:
        ingresos_invalidos += 1
    return resultado, ingresos_validos, ingresos_invalidos    

#inicialización de variables
ruta_archivo = "/home/luci/Documentos/python/logica/Listado_de_persona/personas.txt"
crear_archivo_persona = crear_archivo(ruta_archivo)
personas_modo_lectura = open(ruta_archivo, 'r')
personas = []
lectura_archivo = lectura_del_archivo(personas_modo_lectura, personas)

#nueva apertura del archivo, esta vez para escribirlo
personas_modo_escritura = open(ruta_archivo, 'w')

#ciclo para cargar por teclado de nuevas personas
ingresos_validos = 0
ingresos_invalidos = 0
while True:
    persona = input("Ingrese el apellido y nombre de la persona: ").strip().upper()
    if not persona:
        break
    resultado, ingresos_validos, ingresos_invalidos = validaciones_varias(ingresos_validos, ingresos_invalidos, persona, personas)
    if resultado != (None):
        print(resultado)
print("Ingresos inválidos:", ingresos_invalidos)
print("Personas ingresadas:", ingresos_validos)


#ordenamiento de la lista
personas.sort()

#muestra en pantalla
for p in personas:
    print(p)
  
#escribe cada elemento de la lista en archivo de texto, añadiendo un enter al final de c/u
for p in personas:
    personas_modo_escritura.write(p + '\n')
personas_modo_escritura.close()