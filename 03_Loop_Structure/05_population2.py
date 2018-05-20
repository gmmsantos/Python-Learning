age = 0
while True:
    populationA = int(input("Enter value of population A: "))
    increaseA = float(input("Enter the increase value per year of population A: "))
    populationB = int(input("Enter value of population B: "))
    increaseB = float(input("Enter the increase value per year of population B: "))

    if populationA > populationB:
        while populationB <= populationA:
            populationB *= ((increaseB/100) + 1)
            populationA *= ((increaseA/100) + 1)
            age += 1
    else:
        while populationA <= populationB:
            populationA *= ((increaseA/100) + 1)
            populationB *= ((increaseB/100) + 1)
            age += 1
    if populationA or populationB == 0:
        break
print("It'll take %d years to be same population" %age)