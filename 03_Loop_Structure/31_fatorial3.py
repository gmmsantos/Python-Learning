'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
 A saída deve ser conforme o exemplo abaixo:

    Fatorial de: 5
    5! =  5 . 4 . 3 . 2 . 1 = 120'''

fat = int(input("Enter a number: "))
for i in range(1, fat):
	fat *= i
	
print("Fatorial value is: ", fat)