nota1 = float(input("Informa a nota1: "))
nota2 = float(input("Informe a nota2: "))

m = (nota1+nota2)/2

if m == 10:
    print("GREAT")
elif m >= 7.0:
    print("APPROVED")
else:
    print("REPROVED")
