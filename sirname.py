str="suneel ravi arjun"

x=list(str.split(' '))
temp=" "
for i in x:
    if len(i)==4:
       i=i+" kumar"+temp
    else:
        i=i+" "+temp

    print(i)
