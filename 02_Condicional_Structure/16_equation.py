import math

a = int(input("Informe o valor de A(ax2 + bx + c)"))
b = int(input("Informe o valor de B(ax2 + bx + c)"))
c = int(input("Informe o valor de C(ax2 + bx + c)"))

if a == 0:
    print("Não é uma equação de segundo grau")

else:
    delta = math.pow(b, 2) - (4 * a * c)
    if delta < 0:
        print("Não possui raizes reais")
    elif delta == 0:
        print("Possui somente uma raiz real")
    else:
        print("Delta posito, entao possui duas raizes reais: ")
        raiz1 = (-(b) + math.sqrt(delta)) / (2 * a)
        raiz2 = (-(b) - math.sqrt(delta)) / (2 * a)
        print("Primeira raiz: ", raiz1)
        print("Segunda raiz: ", raiz2)
  