import random

qntd_cpf = input('Quantos CPF quer gerar: ')

for qntd in range(int(qntd_cpf)):
    #GERANDO 9 DIGITOS

    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))

    #PRIMEIRO DIGITO 
    contador_regresivo_1 = 10
    resultado_digito_1 = 0

    for digito in nove_digitos:
        resultado_digito_1 += int(digito)*contador_regresivo_1
        contador_regresivo_1 -= 1

    primeiro_digito = (resultado_digito_1*10)%11
    primeiro_digito = primeiro_digito if primeiro_digito<=9 else 0
    #print(primeiro_digito)

    #SEGUNDO DIGITO
    dez_digitos = nove_digitos+ str(primeiro_digito)
    contador_regresivo_2 = 11
    resultado_digito_2 = 0

    for digito in dez_digitos:
        resultado_digito_2 += int(digito)*contador_regresivo_2
        contador_regresivo_2 -= 1

    segundo_digito = (resultado_digito_2*10)%11
    segundo_digito = segundo_digito if segundo_digito<=9 else 0
    #print(segundo_digito)

    #VALIDAÇÃO DO CPF
    cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
    print('\nCPF GERADO:',cpf_gerado)

