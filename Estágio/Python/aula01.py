pares = 0
impares = 0
zero = 0

qtd = -1

for numero in range(1,6):
  
  try:
    qtd = int(input("Insira um número inteiro:"))

    if qtd == 0: 
      zero = zero + 1
    elif qtd % 2 == 0:
      pares = pares + 1
    else:
      impares = impares + 1
  except:
    print("Deve ser um valor inteiro")
    continue
       

print("A quantidade de números zero é: ", zero)
print("A quantidade de números pares é: ", pares)
print("A quantidade de números impares é: ", impares)