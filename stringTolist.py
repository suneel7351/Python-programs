str="hello how are you"



lis = []
temp = ''
for i in str:
    if i == ' ':
       lis.append(temp)
       temp=''
    else:
        temp=temp+i


if temp:
    lis.append(temp)
print(lis)


