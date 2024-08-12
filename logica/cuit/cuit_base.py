def validar_cuit(cuit):
    '''                                                               '''
    if len(cuit) != 13 or cuit[2] != "-" or cuit[11] != "-":
        return False
    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    cuit = cuit.replace("-", "")
    digito_verificador = 0
    for i in range(10):
        digito_verificador += int(cuit[i]) * base[i]
    digito_verificador = 11 - (digito_verificador - (int(digito_verificador / 11) * 11))
    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = 9
    return digito_verificador == int(cuit[10])

cuit_ingresado = input('Ingrese CUIT (formato ejemplo 20-12345678-9): ')
if validar_cuit(cuit_ingresado) == True:
    print('Está OK')
else:
    print('Error!')