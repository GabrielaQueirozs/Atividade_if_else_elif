lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    
    if lado1 == lado2 and lado2 == lado3:
        print("EQUILÁTERO")
    
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("ISÓSCELES")
    
    else:
        print("ESCALENO")

else:
    print("NÃO FORMA TRIÂNGULO")