numero_str = input("Digite um numero e descubra seu dobro: ")

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float*2}')
except:
    print('Isso não é um número!!')