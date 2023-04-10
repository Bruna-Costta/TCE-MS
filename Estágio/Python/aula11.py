"""Implemente uma função que receba um número inteiro e retorne a quantidade de dígitos que esse número contém."""

def qtd_digitos(numero):
  contador = len(numero)
  return contador

numero = str(input('Informe um numero inteiro: '))
print(qtd_digitos(numero))