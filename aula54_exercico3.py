'''
Faça um programa que peça o primeiro nome do usuario. 
Se o nome tiver 4 letras ou menos escreva  "Seu nome é curto";
Se tiver entre 5 e 6 letras, escreva "Seu nome e normal";
Maior que 6 letras escreva "Seu nome é muito grande"
'''
nome = input('Digite seu nome: ')
nome_qtde = len(nome)
if nome_qtde > 1:
    if nome_qtde <=4 :
        print('Seu nome é curto')
    elif nome_qtde>=5 and  nome_qtde <=6:
        print('Seu nome é normal')
    else:
        print ('Seu nome é grande') 
else:
    print('Digite mais de uma letra')
