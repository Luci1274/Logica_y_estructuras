#inicialización de variables
ruta_archivo = "/home/luci/Documentos/python/logica/Listado_de_persona/personas.txt"
personas_modo_lectura = open(ruta_archivo, 'r')
ingresos_validos = 0
ingresos_invalidos = 0
personas = [] 

#lectura secuencial del archivo y carga en lista personas, quitandole el enter al final de cada uno
while True:
    persona = personas_modo_lectura.readline()
    if not persona:
        break
    personas.append(persona[:-1])
personas_modo_lectura.close()

#nueva apertura del archivo, esta vez para escribirlo
personas_modo_escritura = open(ruta_archivo, 'w')

#ciclo para cargar por teclado de nuevas personas
while True:
    persona = input("Ingrese el apellido y nombre de la persona: ").strip().upper()
    if not persona:
        break
    
    #validaciones varias: solo texto, 2 o mas palabras y no repetido
    ok = True
    for caracter in persona:
        if caracter.isdigit():
            ok = False
            print('Solo se permiten letras')
            break
        
    if len(persona.split()) == 1:
        ok = False
        print('Debería ingresar Apellido y Nombre/s')

    if persona in personas:
        ok = False
        print('El persona ya fue ingresado')        

    if ok:
        personas.append(persona)
        ingresos_validos += 1
    else:
        ingresos_invalidos += 1

print("Ingresos inválidos:", ingresos_invalidos)
print("Personas ingresadas:", ingresos_validos)

#ordenamiento de la lista
personas.sort()

#muestra en pantalla
for alumno in personas:
    print(alumno)
  
#escribe cada elemento de la lista en archivo de texto, añadiendo un enter al final de c/u
for alumno in personas:
    personas_modo_escritura.write(alumno + '\n')
personas_modo_escritura.close()