num = 875965
count = 0
temp=num
while num != 0:
    num = int(num/10)
    count += 1
    
print("{} digit present in {} ".format(count,temp))
