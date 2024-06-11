nome = input('Digite seu nome: ') 
idade = input ('Digite sua idade: ')

if nome and idade :
    print(f'')
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido {nome[::-1]}')

    if '' in nome:
        print('Seu nome contém espaços')
    else:
       print('Seu nome contém não espaços')
    
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
   print ('Desculpe voçê deixou campos vazios')
