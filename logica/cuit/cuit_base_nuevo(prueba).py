import datetime

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

while True:

    cuit_ingresado = input('\nIngrese CUIT (ejemplo 20123456789) o <Enter> para salir: ').strip()
    if not cuit_ingresado:
        break
    elif not cuit_ingresado.isdigit():
        print(mensajes[1])
        continue

    cuit_valido, digito_obtenido, largo_correcto = validar_cuit(cuit_ingresado)

    if largo_correcto:
        prefijo = cuit_ingresado[:2]
        documento = cuit_ingresado[2:10]
        sufijo = cuit_ingresado[10]
    else:
        print(mensajes[2], "Debe ingresar 11 dígitos!")
        continue

    cuit_formateado = prefijo + "-" + documento + "-" + sufijo     
    if largo_correcto and cuit_valido:
        print('El CUIT', cuit_formateado, mensajes[3])
    elif largo_correcto and not cuit_valido:
        print('CUIT', cuit_formateado, "es incorrecto.",mensajes[4], "debería ser", digito_obtenido)

    if prefijo not in todas_las_personas:
        print(mensajes[5], "Los posibles son:", end=' ')
        for posibles_prefijo in todas_las_personas:
            print(posibles_prefijo, end=' ')
        continue

    if prefijo in personas_fisicas:
        tipo_persona = 'f'
    elif prefijo in personas_juridicas:
        tipo_persona = 'j'
    print('El CUIT ingresado corresponde a una persona', tipo_persona)

    try:
        archivo = open("logica/cuit/cuit.log", "w")
        archivo.write(cuit_ingresado, mensajes, cuit_formateado,prefijo,datetime)
        archivo.close
    except:
        pass