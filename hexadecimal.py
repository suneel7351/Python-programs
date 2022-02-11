table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
rem=0
decimal = 78
hexa = ''

while(decimal>0):
    rem = decimal%16
    hexa =table[rem]+ hexa
    decimal = decimal//16
    
print(hexa)
