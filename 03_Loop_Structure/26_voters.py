quantidade = int(input("Informe quantos eleitores: "))
t1=t2=t3 = 0

for i in range(0, quantidade): 
    voto = int(input("Eleitor %d \nInforme em quem vc vota(Candidato 1, ou 2, ou 3): " %i))
    if voto == 1:
        t1 += 1
    elif voto == 2:
        t2 += 1
    else:
        t3 += 1

print("Votos Candidato 1: ", t1)
print("Votos Candidato 2: ", t2)
print("Votos Candidato 3: ", t3)