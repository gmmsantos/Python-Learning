turma = int(input("Informe quantas turmas existem: "))

total = 0
for i in range(0, turma):
    alunos = -1
    while (alunos < 0) or (alunos > 40):
        alunos = int(input("Informe quantos alunos existem na %da turma: " %(i+1)))
        if (alunos < 0) or (alunos > 40):
            print("Só podem ter no maximo 40 alunos por turma, informe outro valor")
    total += alunos

print("A media de alunos por turma: %d" %((total/turma)+1))