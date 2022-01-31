def filterNum(n):
    return n>='0' and n<='9'
x=[]
print("Enter the value of n ")
n=int(input())
for i in range(0,n):
      i=input("Enter the values = ")
      x.append(i)

filterInput=list(filter(filterNum,x))
print(filterInput)
