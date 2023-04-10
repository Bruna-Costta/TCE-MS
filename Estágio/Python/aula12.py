"""
Implemente uma função que retorne o reverso de um número inteiro informado. Por exemplo: Informado - 411 | Retorno - 114.
"""

def reverso(numero):
  numero = str(numero)
  print(numero[::-1])

numero = int(input("Digite: "))
reverso(numero)