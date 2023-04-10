"""
Implemente um código que peça 10 números inteiros, calcule e mostre a quatidade de um números pares e a quantidade 
de números impares. Se for 0 contabilize como quantidade de números ZERO.
"""

pares = 0
impares = 0
zero = 0
for numero in range(1,10):
  qtd = int(input("Insira um número inteiro:"))

  if qtd == 0: 
    zero = zero + 1
  elif qtd % 2 == 0:
    pares = pares + 1
  else:
    impares = impares + 1 
       

print("A quantidade de números zero é: ", zero)
print("A quantidade de números pares é: ", pares)
print("A quantidade de números impares é: ", impares)