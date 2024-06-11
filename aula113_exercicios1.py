def multiplacar (*args):
    total = 1
    for numero in args:
        total *= numero
    
    return total

numeros = 2, 2
resultado = multiplacar(*numeros)
print(resultado)
