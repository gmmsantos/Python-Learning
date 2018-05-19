wage = float(input("Informe seu salario:"))
if wage > 900.00 and wage <= 1500.00:
    ir = wage * 0.05
    p = 5
elif wage > 1500.00 and wage <= 2500:
    ir = wage * 0.1
    p = 10
elif wage > 2500.00:
    ir = wage * 0.2
    p = 20
else:
    print("Isento")
    ir = 0
    p = 0

print("Salario Bruto:                  : R$", wage)
print("(-) IR %d %                     : R$ %f" %(i ,r))
print("(-) INSS (10%)                  : R$", wage*0.1)
print("FGTS (11%)                      : R$", wage*0.11)
print("(-) Sindicato (3%)              : R$", wage*0.03)
print("Total de descontos              : R$", ir+(wage*0.1)+(wage*0.03))
print("Salario Liquido                 : R$", wage-(ir+(wage*0.1)+(wage*0.03)))
