"""
Implemente um código que solicite para N pessoas a sua idade, onde N é um valor inteiro informado pelo usuário. 
Ao final o programa verifique se a média de idade da turma varia entre 0 e 25 (turma jovem), 26 e 60 (turma adulta) e 
maior que 60 (melhor idade). Imprima no final uma relação de todas as pessoas, onde para cada pessoa apareça 
“idade - pertence a turma {nome_turma}”. Após essa relação de pessoas, imprima a média de idade da turma e qual variação 
etária a turma pertence. OBS: Para esse exercício poderá ser utilizado if, else, while, for, etc., quando achar necessário.
"""

qtd_pessoas = int(input("Informe a quantidade de alunos: "))
contador = 0
soma_idade = 0
aluno = 1

while contador < qtd_pessoas:
  idade = int(input(f"Informe a idade do aluno {aluno}: "))
  soma_idade = soma_idade + idade
  contador = contador + 1
  aluno = aluno + 1

  if (idade >= 1 and idade <= 25):
     print(f'A idade do aluno é {idade} e sua turma será Jovem')
  elif (idade >= 25 and idade <= 60):
     print(f'A idade do aluno é {idade} e sua turma será Adulta')
  elif (idade >= 60):
     print(f'A idade do aluno é {idade} e sua turma será Melhor idade')

media_idade = soma_idade / qtd_pessoas
print("A média de idade é de: ", media_idade)

if 0 <= media_idade <= 25:
    print('A variação etaria das turmas é Turma Jovem')

elif 26 <= media_idade <= 60:
    print('A variação etaria das turmas é Turma Adulta')

else:
    print('A variação etaria das turmas é Melhor Idade')
