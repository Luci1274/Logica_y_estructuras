from datetime import datetime
ahora = datetime.now()
def otro_cuit():
    """pregunta si se desea introducir otro cuit"""
    while True:
        try:
            otro_cuit = input("Ingresar otro cuit (S/N)? ").strip().lower()
            if otro_cuit == 's':
                return True
            elif otro_cuit == 'n':
                return False
        except:
            print("por favor escriba s/n")

def validar_cuit(cuit):
    '''Valida que el dato ingresado tenga el formato de 11 digitos
    retornando 3 datos: si el cuit es válido, el dígito verificador
    y si el largo es correcto o no.'''
    if len(cuit) == 11:
        base = (5, 4, 3, 2, 7, 6, 5, 4, 3, 2)
        digito_verificador = 0
        for i in range(10):
            digito_verificador += int(cuit[i]) * base[i]
        digito_verificador = 11 - (digito_verificador - (int(digito_verificador / 11) * 11))
        if digito_verificador == 11:
            digito_verificador = 0
        elif digito_verificador == 10:
            digito_verificador = 9
        return digito_verificador == int(cuit[10]), digito_verificador, True
    else:
        return False, 0, False


#cuerpo principal del programa
personas_fisicas = '20', '23', '24', '25', '27'
personas_juridicas = '30', '33', '34'
todas_las_personas = personas_fisicas + personas_juridicas

mensajes ={1:"Solo se aceptan dígitos numéricos",
    2: "Largo de CUIT incorrecto",
    3:"Cuit OK",
    4:"Dígito verificador incorrecto", 
    5:"Prefijo incorrecto"}

try:
    cuit_log = open("logica/cuit/cuit.log", "x")
    cuit_log.close()
except:
    pass
cantidad_de_cuit = 1
cuit_correcto = 0
cantidad_fisica = 0
cantidad_juridica = 0
while True:

    cuit_ingresado = input('\nIngrese CUIT (ejemplo 20123456789) o <Enter> para salir: ').strip()
    cuit_log = open("logica/cuit/cuit.log", "a")
    cuit_log.write("\n" + cuit_ingresado + ", " )
    cuit_log.close()
    if not cuit_ingresado:
        break
    elif not cuit_ingresado.isdigit():
        cuit_log = open("logica/cuit/cuit.log", "a")
        cuit_log.write("1" + ", " )
        cuit_log.close
        print(mensajes[1],)
        pregunta = otro_cuit()
        if pregunta == True:
            cantidad_de_cuit += 1
            continue
        else:
            break
    elif cuit_ingresado == "00000000000":
        print(cantidad_de_cuit, cuit_correcto, cantidad_fisica, cantidad_juridica)
        pregunta = otro_cuit()
        if pregunta == True:
            cantidad_de_cuit += 1
            continue
        else:
            break


    cuit_valido, digito_obtenido, largo_correcto = validar_cuit(cuit_ingresado)

    if largo_correcto:
        prefijo = cuit_ingresado[:2]
        documento = cuit_ingresado[2:10]
        sufijo = cuit_ingresado[10]
    else:
        cuit_log = open("logica/cuit/cuit.log", "a")
        cuit_log.write("2" + ", " )
        cuit_log.close()
        print(mensajes[2], "Debe ingresar 11 dígitos!")
        pregunta = otro_cuit()
        if pregunta == True:
            cantidad_de_cuit += 1
            continue
        else:
            break

    cuit_formateado = prefijo + "-" + documento + "-" + sufijo     
    if len(cuit_formateado) >= 3:
        cuit_log = open("logica/cuit/cuit.log", "a")
        cuit_log.write (str(cuit_formateado + ", " ))
        cuit_log.close()
    else:
        pass

    if largo_correcto and cuit_valido:
        cuit_log = open("logica/cuit/cuit.log", "a")
        cuit_log.write("3" + ", " )
        print('El CUIT', cuit_formateado, mensajes[3])
        
    elif largo_correcto and not cuit_valido:
        cuit_log.write("4" + ", " )
        print('CUIT', cuit_formateado, "es incorrecto.",mensajes[4], "debería ser", digito_obtenido)
        pregunta = otro_cuit()
        if pregunta == True:
            cantidad_de_cuit += 1
            continue
        else:
            break
        

    if prefijo not in todas_las_personas:
        cuit_log = open("logica/cuit/cuit.log", "a")
        cuit_log.write("5" + ", ")
        cuit_log.close()
        print(mensajes[5], "Los posibles son:", end=' ')
        for posibles_prefijo in todas_las_personas:
            print(posibles_prefijo, end=' ')
        pregunta = otro_cuit()
        if pregunta == True:
            cantidad_de_cuit += 1
            continue
        else:
            break

    if prefijo in personas_fisicas:
        tipo_persona = 'f'
        cantidad_fisica += 1
    elif prefijo in personas_juridicas:
        tipo_persona = 'j'
        cantidad_juridica += 1
    print('El CUIT ingresado corresponde a una persona', tipo_persona)

    cuit_log.write(prefijo + ", ")
    cuit_log.close()
    cuit_log = open("logica/cuit/cuit.log", "a")
    cuit_log.write(str(ahora))
    cuit_log.close ()   
    pregunta = otro_cuit()
    if pregunta == True:
        cuit_correcto += 1
        cantidad_de_cuit += 1
        continue
    else:
        break