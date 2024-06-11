while True:
    print('CALCULADORA\n')
    n1 = input('Digite um valor: ')
    operador = input('Escola uma operação - (+) (-) (*) (/): ')
    n2 = input ('Digite outro valor: ')
    
    try:
        n1_float = float(n1)
        n2_float = float(n2)
        numeros_validos=True

        if operador == '+':
            resultado = n1_float + n2_float
            print(f'Resultado {n1_float} {operador} {n2_float} = {resultado}\n')
        elif operador == '-':
            resultado = n1_float - n2_float
            print(f'Resultado {n1_float} {operador} {n2_float} = {resultado}\n')
        elif operador == '*':
            resultado = n1_float * n2_float
            print(f'Resultado {n1_float} {operador} {n2_float} = {resultado}\n')
        elif operador == '/':
            resultado = n1_float / n2_float
            print(f'Resultado {n1_float} {operador} {n2_float} = {resultado:2f}\n')
    except:
        numeros_validos = None
       
    if numeros_validos is None:
        print('Um ou ambos numeros digitados são invalidos.')
        continue

    operadores_permitidos='+-*/'

    if operador not in operadores_permitidos:
        print('Operador inavalido\n')
        continue
    if len(operador)>1:
        print('Digite apenas um operador\n')
        continue

        
    sair = input('Quer Sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break