"""
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este número e par ou impar. Caso o usuario não digite um numero
inteiro, informe que não é um numero inteiro.
"""


valor = input('Digite um numero inteiro: ') 


if valor.isdigit():
    valor_int = int(valor)
    par_impar = valor_int %2 == 0
    par_impar_texto= 'impar'
    if par_impar:
        par_impar_texto = 'par'
    
    print(f'O numero {valor_int} é {par_impar_texto}')
    
else:
    print('Não é um numero inteiro')
