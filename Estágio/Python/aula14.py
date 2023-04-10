"""
Implemente uma função que receba uma string como parâmetro e retorne outra string com os carateres embaralhados. 
Ex.: Informado - Tribunal | Retorno - ritunbal. Esse embaralhamento deve ocorrer de forma aleatória. 
Utilize a função lower() dentro da sua função para padronizar todas as strings recebidas para minúsculo. 
Após implementar sua função, pergunte ao usuário qual palavra ele quer embaralhar, e quantas vezes ele quer 
embaralhar essa palavra, retorne a mesma string embaralhada a quantidade de vezes que o usuário quiser. 
Dica: (coloque sua função dentro de um While repentindo o laço a quantidade de vezes que o usuário solicitou, 
como já fizemos em exercícios passados).
"""

from random import shuffle

def embaralha(nome):
    a = list(nome)
    shuffle(a)
    a = ''.join(a)
    print(a.lower())


nome = input('Digite: ')
embaralha(nome)