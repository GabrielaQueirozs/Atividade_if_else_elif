preco = float(input("Preço: R$ "))

opcao = int(input("Opção: "))

if opcao == 1:
    valor_final = preco - (preco * 10 / 100)

elif opcao == 2:
    valor_final = preco - (preco * 5 / 100)

elif opcao == 3:
    valor_final = preco

elif opcao == 4:
    valor_final = preco + (preco * 8 / 100)

else:
    print("Opção inválida")
    valor_final = None

if valor_final is not None:
    print(f"Valor final: R$ {valor_final:.2f}")