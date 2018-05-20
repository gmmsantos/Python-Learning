while True:
    nota = float(input("Enter a valid school grade: "))
    if nota >= 0 and nota <= 10:
        print("Valid: ", nota)
        break
    else:
        print("Invalid value,type again!")
