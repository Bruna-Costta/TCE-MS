"""
Implemente uma função chamada "verifica_positivo" que que receba um número como argumento. 
A função deve retornar True se o número informado for positivo, e False se o número informado for zero ou negativo.
"""

def verifica_positivo(valor):
  return valor > 0

valor = int(input('Digite o valor:'))
num = verifica_positivo(valor)
print(num)