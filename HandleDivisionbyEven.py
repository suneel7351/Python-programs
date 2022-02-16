try:

    x = int(input("Enter a number : "))
    y = int(input("Enter a number with which you want to divide : "))
    result = x/y
    if (y % 2 != 0):
        print(result)
    else:
        raise Exception("Don't divide by even number")
except Exception():
    print(Exception())
