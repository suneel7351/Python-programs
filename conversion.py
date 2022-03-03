decimal = int(input("Enter a decimal value : \n"))
conversion = int(input("Enter 1 for Binary , 2 for Octal and 3 for Hexa : "))


def hexa(n):
    table = ['0', '1', '2', '3', '4', '5', '6',
             '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    hexa = ''
    while(n > 0):
        rem = 0
        rem = n % 16
        hexa = table[rem] + hexa
        n = n//16

    return hexa


def octa(n):
    octList = []
    i = 0
    while n > 0:
        octList.append(n % 8)
        n = n//8
    return octList


def binary(n):
    binList = []
    i = 0
    while n > 0:
        binList.append(n % 2)
        n = n//2

    return binList


if conversion == 1:
    # y = binary(decimal)
    print("Binary of {} is :".format(decimal))
    for x in binary(decimal)[::-1]:
        print(x)
elif conversion == 2:
    y = octa(decimal)
    print("Octa of {} is :".format(decimal))
    for x in y[::-1]:
        print(x)
elif conversion == 3:
    print("Hexa of {} is {} ".format(decimal, hexa(decimal)))
