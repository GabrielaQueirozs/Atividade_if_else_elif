peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura * altura)

if imc < 18.5:
    classificacao = "ABAIXO DA FAIXA"
elif imc < 25.0:
    classificacao = "FAIXA NORMAL"
elif imc < 30.0:
    classificacao = "ACIMA DA FAIXA"
else:
    classificacao = "FAIXA ELEVADA"

print(f"IMC: {imc:.1f}")
print(f"Classificação: {classificacao}")