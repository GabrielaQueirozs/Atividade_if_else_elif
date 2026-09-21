nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
media = (nota1 + nota2) /2
print(f"sua média é: {media:.2f}")
if media >=7 :
    print("Você está aprovado!")
elif 5 <= media <= 7:
    print("Recuperação")
else:
    print("Reprovado")        