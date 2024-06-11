import os

letras_acertadas = ''
num_tentativas = 0
palavra_secreta = input('Escolha a palavra secreta: \n')
os.system('clear')

while True:
    letra_digitada = input('\nDigite uma letra: ')
    os.system('clear')
    num_tentativas +=1

    if len(letra_digitada)>1:
        print('\nDigite apenas uma letra!!')
        continue 
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
             palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('\nPalavra formada: ',palavra_formada)

    if palavra_formada == palavra_secreta:
        print('\nVocê ganhou! Parabéns!')
        print('Palavra secreta era:',palavra_secreta)
        print('Tentativas:',num_tentativas)
        letras_acertadas = ''
        num_tentativas = 0
        palavra_secreta = input('\nEscolha a palavra secreta: \n')
        os.system('clear')


