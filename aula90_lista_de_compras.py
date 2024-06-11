import os

lista_compras = []
while True:
   
    opcao = input('\nSelecione uma opção\n[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('clear')
        item = input('\nQual item deseja adicionar a lista: ')
        lista_compras.append(item)
    
    elif opcao == 'a':

        indice_str = input('\nEscolha o indice para apagar: ')

        try: 
            indice = int(indice_str)
            del lista_compras[indice]

        except ValueError:
            print('Por favor digite numero int')
        except IndexError:
            print('Indice não existe na lista. ')
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l':
        os.system('clear')

        if len(lista_compras) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista_compras):
            print(i, valor)
        
    else:
        print('Por favor, escolha i ou l.')