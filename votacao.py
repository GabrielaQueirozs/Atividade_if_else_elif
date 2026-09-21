idade = int(input("Digite a sua idade: "))

if idade <= 15:
    print("Não pode votar!")
elif idade >= 16 and idade <= 17:
    print("Voto opcional!")
elif idade >= 18 and idade <= 69:
    print("Voto obrigatório!")
else:
    print("Voto opcional!")