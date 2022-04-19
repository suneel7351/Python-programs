from math import sqrt
n = int(input("Enter a number : "))
prime = 0

if(n >= 1):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            prime = 1
            break
    if (prime == 0):
        print("prime")
    else:
        print("Not Prime")
