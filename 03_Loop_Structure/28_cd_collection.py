'''Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um. '''

totalcd = 0
totalprice = 0

while True:
	cd = int(input("Enter the amount of CDs: "))	
	if cd == 0:
		break
	else:
		price = float(input("Enter the value paid: "))
		totalcd += cd
		totalprice += price
print("The average price is: ", totalprice/totalcd)	
print("Total is: $", totalprice)	

