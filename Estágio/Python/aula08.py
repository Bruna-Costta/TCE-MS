"""
Adicione uma nova funcionalidade ao exercício 3, não permitindo que o usuário digite algo diferente de número inteiro. 
Quando digitar algo diferente de inteiro exiba na tela que deve ser um número inteiro e solicite a informação novamente. 
Apresente também no final a porcentagem de números pares, ímpares e zeros.
dica: type(variavel) = int
"""

pares = 0
impares = 0
zero = 0

qtd = -1

for numero in range(1,11):
  
  try:
    qtd = int(input("Insira um número inteiro:"))

    if qtd == 0: 
      zero = zero + 1
    elif qtd % 2 == 0:
      pares = pares + 1
    else:
      impares = impares + 1
  except:
    print("Deve ser um valor inteiro")
    continue

total  = pares + impares + zero
porcentagemPar = pares / total * 100
porcentagemImpar = impares / total * 100
porcentagemZeros = zero / total * 100
print('-'*45)
print("A quantidade de números zero é: ", zero)
print("A quantidade de números pares é: ", pares)
print("A quantidade de números impares é: ", impares)
print('-'*45)
print('Porcentagem de números pares é: ', porcentagemPar)
print('Porcentagem de números impares é: ', porcentagemImpar)
print('Porcentagem de números impares é: ', porcentagemZeros)