#def f1():
   # a=int(input("enter first number"))
   # b=int(input("enter second number"))
   # c=a+b
   # print(c)
#f1()

#def f2(a,b):
      #c=a+b
     # return c

#x=int(input("Enter first num "))
#y=int(input("enter second num"))
#c=f2(x,y)
#print(c)


#default params

#def f2(x=4,y=2):
#here f2 make a dictionary where x and y key and 4,6 values
  # z=x*y
  # return z
#f2(6)

#print(f2(6))

#contro arguments position

#def f2(x,y):
 #  z=x-y
  # return z


#print(f2(y=9,x=3))



#we can pass a function as a function params

#def f4(p):
  #  return p**2
#def f1(x,y,f2):
    #z=f2(x)**f2(y)
    # return z
#print(f1(2,2,f4))


def f1(*ar):
#this function make tupple
       print(ar[0],ar[1],ar[2])
#f1((2,3,4))


#jhan bhi blank body rkhna ho wha pass use krenge

#def f1():
#     pass
     
#if 5>4:
#   pass
   
#for i in range(0,9):
 #  pass
 
 
 #recursion
#def f1(x):
#    if x<=0:
 #    return 1
#    else:
#     return x*f1(x-1)
#print(f1(5))

#arbitary keyword argument
#kon kon se keywords function me use ho rhe hain

#def f1(**kw):
#kw naame ki ek dictionary bnegi jo key vlaue pair rkhti hai
   # ke=list(kw.keys())
#keys() function ek dictionary list bnata hai
#ke me list of keys
  #  print(ke)
    #print(kw['fname'])
   # print(kw[ke[1]])
#f1(fname="hari",lname="krishna",mname="govind")


# we can pass list as a param
#def f1(x):
  #x[2]=5
  #print(x[1])
#y=[1,2,3,4]
#f1(y) 
#print(y)
#this type of function calling is call by ref
  
  
#module is a file in which written different different functions defination
#just like header files in c


#import module
#p=module.pow(2,2)
#print(p)
#s=module.square(4)
#print(s)

#x=[4,5,1,7]
#map function return an object
#map ek given list ko function me apply krta hai
#y=map(module.square,x)
#print(list(y))

#list comprehension
# isme 3 segment hote hain
#[map,generator,filter]
#i=[module.square(x) for x in range(100) if x%2==0]
#for x in range(100) generator generate a sequence
#if x%2==0 0 to 100 me filter hongi value
#fir map function apply kr dega
#print(i)
#i=[module.square(x) for x in [1,2,3,4]]
#print(i)

