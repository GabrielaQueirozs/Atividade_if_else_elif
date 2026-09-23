valor_ingresso = 30.00

idade = int(input("Idade: "))
estudante = input("Estudante (SIM/NÃO): ").strip().upper()

if idade < 12 or estudante == "SIM" or idade >= 60:
    valor_final = valor_ingresso * 0.50
else:
    valor_final = valor_ingresso

print(f"Valor do ingresso: R$ {valor_final:.2f}".replace(".", ","))
