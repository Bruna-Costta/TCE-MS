notas = [[2, 3, 5, 10], 8, [5, 2, 1, 9],[6, 8, 7, 1]]
soma = 0
aluno = 1

string = 'Relação dos alunos aprovados (acima de 5.0):'
print(string)
print('-'*len(string))

for grupo_nota in notas:
  if type(grupo_nota) != list or len(grupo_nota) != 4:
    print(f'Aluno {aluno} = Formáto inválido')
    aluno += 1
  else:
    for nota in grupo_nota:
      soma = soma + nota
    media = soma/4

    if media >= 5:
      print(f'Aluno {aluno} = {media}')
    else:
      print(f'Aluno {aluno} = REPROVADO')
  
  soma = 0
  aluno += 1