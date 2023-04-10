numero = input()

try:
    if type(eval(numero)) == type(1):
        print("tipo inteiro")
    elif type(eval(numero)) == type(1.0):
        print("tipo real")
    else:
        print('não é um tipo numérico, %s' % type(numero))
except NameError as n:
    print('não é um tipo numérico, %s' % type(numero))