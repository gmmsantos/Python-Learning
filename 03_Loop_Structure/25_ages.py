quantidade = int(input("Numero de pessoas: "))

total = 0
for i in range(1, quantidade+1):
    idade = int(input("Informe a idade da %da pessoa" %i))
    if idade <= 0:
        print("Idade tem que ser maior que 0")
    total += idade

if 0 <= total/quantidade <= 25:
    print("Turma jovem.")
elif 26 <= total/quantidade <= 60:
    print("Turma adulta.")
else:
    print("Turma idosa")