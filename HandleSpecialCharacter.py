

try:
    name = input("Enter your name : ")
    for i in name:
        if(ord(i) >= 32 and ord(i) <= 47) or (ord(i) >= 58 and ord(i) <= 64) or (ord(i) >= 91 and ord(i) <= 96) or (ord(i) >= 123 and ord(i) <= 127):
            raise Exception
            break

    print("Your name is {}".format(name))


except:
    print("Dont't use special character in string")
