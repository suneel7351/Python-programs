decimal=int(input("Enter a decimal value : \n"))
conversion=int(input("Enter 1 for Binary , 2 for Octal and 3 for Hexa :\n"))

if conversion == 1:
	print("Binary of {} is {} ".format(decimal,bin(decimal)))
elif conversion==2:
	print("Octal of {} is {} ".format(decimal,oct(decimal)))
elif conversion==3:
	print("Hexa of {} is {} ".format(decimal,hex(decimal)))
