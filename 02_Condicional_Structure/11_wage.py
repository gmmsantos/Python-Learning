salario = float(input("Informe seu salario: "))
print("Seu salário antes do reajuste é: ", salario)

if salario <= 280.00:
    salario1 = salario * 1.2
    print("Voce recebeu um aumento de 20%")
elif salario > 280.00 and salario <= 700.00:
    salario1 = salario * 1.15
    print("Voce recebeu um aumento de 15%")
elif salario > 700.00 and salario <= 1500.00:
    salario1 = salario * 1.1
    print("Voce recebeu um aumento de 10%")
else:
    salario1 = salario * 1.05
    print("Voce recebeu um aumento de 5%")

print("Voce teve um acrescimo de:", salario1-salario)
print("Seu novo salario eh:", salario1)
