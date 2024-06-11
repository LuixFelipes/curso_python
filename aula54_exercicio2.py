"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horário
descrito, exiba a saudação apropiada, Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = input('Digite a hora: ')


try:
    horas_float = float(horas)
    if horas_float >= 0 and horas_float<=11.59:
        print('Bom Dia ')
    elif horas_float >= 12 and horas_float<=17.59:
        print('Boa Tarde')
    elif horas_float >= 18 and horas_float<=23.59:
        print('Boa Noite')
except: 
    print('Valor incorreto')