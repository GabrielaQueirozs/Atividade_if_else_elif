## Exercicio maior ou menor de três números
## leia três números reais e mostre o maior e menor valor informado


## pedir ao usuário 3 números
## float é para números décimais e vírgulas
## Input para o usuário dar a informação
n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))
n3 = float(input("Digite o terceiro número:"))


## ess pimeiro código só se for MAIOR
## se o primeiro número for maior que o segundo e maior que o 
# terceiro o maior número será o PRIMEIRO
if n1 >= n2 and n1 >= n3:
    maior = n1
# Se o segundo número for maior que o primeiro e maior que o terceiro
# o maior número será o TERCEIRO    
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n2

## Esse segundo código mostra só se for menor
# Se o número 1 for menor ou igual o segundo número e menor que o terceiro
# o menor número será o PRIMEIRO
if n1 <= n2 and n1 <= n3:
  menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else:
    menor = n3

print("Maior:",maior) 
print("Menor:",menor)         