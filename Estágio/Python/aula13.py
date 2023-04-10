"""
Implemente uma função que receba uma data no formato DD/MM/AAAA e devolva uma string com a seguinte estrutura: 
"dia de mesPorExtenso de AAAA (Ex.: Informado: 26/09/2022 | Retorno: 26 de setembro de 2022). 
Caso a data informada para a função esteja fora do padrão, retorne a string "data informada não está no padrão".
"""

def data_extenso(data):
  meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

data = input("Informe a data (dd/mm/aaaa): ")

print (data.split("/")[0], "de", meses[(int(data.split("/")[1])-1)], "de", data.split("/")[2])