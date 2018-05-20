quantidade = 0
while (quantidade <= 0):
    quantidade = int(input("Voce quer saber a media de quantas notas: "))
    if (quantidade <= 0):
        print("A quandidade deve ser positiva")
              
i= 1
total = 0
while i <= quantidade:
    nota = float(input("Informe a %d nota: " %i))
    total += nota
    i += 1

print("Media aritmetica: %.2f" %(total/quantidade))