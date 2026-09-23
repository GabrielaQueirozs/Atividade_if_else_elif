salario = float(input("Digite o salário atual: R$ "))

if salario <= 1500:
    percentual = 15
elif salario <= 3000:
    percentual = 10
else:
    percentual = 5

aumento = salario * percentual / 100
novo_salario = salario + aumento

print(f"Percentual aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")