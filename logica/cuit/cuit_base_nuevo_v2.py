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

def terminar_cuit (cuit_valido, digito_obtenido, largo_correcto):
    personas_fisicas = '20', '23', '24', '25', '27'
    personas_juridicas = '30', '33', '34'
    todas_las_personas = personas_fisicas + personas_juridicas
    while True:
        cuit_valido, digito_obtenido, largo_correcto = validar_cuit(cuit_ingresado)

        if largo_correcto:
            prefijo = cuit_ingresado[:2]
            documento = cuit_ingresado[2:10]
            sufijo = cuit_ingresado[10]
        else:
            print('El largo del CUIT ingresado NO es correcto. Debe ingresar 11 dígitos!')
            continue

        cuit_formateado = prefijo + "-" + documento + "-" + sufijo     
        if largo_correcto and cuit_valido:
            print('El CUIT', cuit_formateado, 'está OK.')
        elif largo_correcto and not cuit_valido:
            print('CUIT', cuit_formateado, 'es incorrecto. El dígito verificador debería ser', digito_obtenido)

        if prefijo not in todas_las_personas:
            print('Prefijo incorrecto. Los posibles son:', end=' ')
            for posibles_prefijo in todas_las_personas:
                print(posibles_prefijo, end=' ')
            continue

        if prefijo in personas_fisicas:
            tipo_persona = 'física.'
        elif prefijo in personas_juridicas:
            tipo_persona = 'jurídica.'
        print('El CUIT ingresado corresponde a una persona', tipo_persona)
    

while True:
    cuit_ingresado = input('\nIngrese CUIT (ejemplo 20123456789) o <Enter> para salir: ').strip()
    if not cuit_ingresado:
        break
    elif not cuit_ingresado.isdigit():
        print('Solo se aceptan dígitos numéricos!')
        continue