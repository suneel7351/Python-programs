import os

print(os.getcwd())
os.chdir("/home/suneel/Desktop")


print(os.getenv("USER"))


os.putenv("name","suneel rajput")

print(os.getenv("name"))

print(os.uname())



# os.fchmod(objectOfFile,"ugo+per") change permission u means owner ,g means gruop user ,o means other user
# + means add persmission 
# - means remove permission


# os.fchown(objectofFile,userid,grpid)


# os.getgroups()
# os.getgrouplist()

print(os.getgroups())
print(os.getgrouplist("suneel",30))

