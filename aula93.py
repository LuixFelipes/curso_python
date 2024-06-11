'''
split e join com list e str
split - divide uma strig
join - une uma string
strip - corta os espaços da string
'''

frase = 'Olha só que, coisa interessante'

#lista_palavras = frase.split()
lista_frase_crua = frase.split(',')
lista_frase = []

for i, frase in enumerate(lista_frase_crua):
    lista_frase.append(lista_frase_crua[i].strip())

print(lista_frase)

frases_unidas = '-'.join(lista_frase)
print(frases_unidas)

