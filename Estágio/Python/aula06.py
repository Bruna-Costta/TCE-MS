"""
Implemente um código que receba dois número inteiros e gere os número inteiros que estão no intervalo entre esses números.
"""

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

for contador in range(n1, n2, 1):
  print(contador)