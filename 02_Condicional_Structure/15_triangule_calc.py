L1 = int(input("Informe o tamanho do Lado1 do Tringulo: "))
L2 = int(input("Informe o tamanho do Lado2 do Tringulo: "))
L3 = int(input("Informe o tamanho do Lado3 do Tringulo: "))

if (L1+L2) > L3 or (L1+L3) > L2 or (L2+L3) > L1:
    triangulo = True

if triangulo:
    print("Os valores formam um triangulo")
    if L1 == L2 == L3:
        print("Triangulo Equilátero")
    elif L1 == L2 or L1 == L3 or L2 == L3:
        print("Triangulo Isosceles")
    else:
        print("Triangulo Escaleno")
else:
    print("Os valores não formam um triangulo")