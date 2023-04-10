"""
Implemente um código que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

usuario = str(input("Informe seu nome: "))
senha = str(input("Senha: "))

while usuario == senha:
  print("Campos Usuário e Senha não podem ser iguais!")
  usuario = str(input("Usuário: "))
  senha = str(input("Senha: "))
else:
  print("Cadastrado com sucesso!")