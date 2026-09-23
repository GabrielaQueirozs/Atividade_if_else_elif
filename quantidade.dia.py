mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if mes < 1 or mes > 12:
    print("MÊS INVÁLIDO")

elif mes == 2:
    if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
        print("29 dias")
    else:
        print("28 dias")

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("30 dias")

else:
    print("31 dias")