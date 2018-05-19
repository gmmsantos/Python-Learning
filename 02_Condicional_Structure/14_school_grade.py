nota1 = float(input("Informe a nota da primeira prova"))
nota2 = float(input("Informe a nota da segunda prova"))

media = (nota1+nota2)/2
print("Sua media é:", media)

if media >= 9.0:
    print("Seu conceito é A")
    aprovado = True
elif media >= 7.5 and media < 9.0:
    print("Seu conceito é B")
    aprovado = True
elif media >= 6.0 and media < 7.5:
    print("Seu conceito é C")
    aprovado = True
elif media >= 4.0 and media < 6.0:
    print("Seu conceito é D")
    aprovado = False
else:
    print("Seu conceito é E")
    aprovado = False
    
if aprovado:
    print("APROVADO")
else:
    print("REPROVADO")