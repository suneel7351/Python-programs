emp=[
{
"name":"suneel",
"empId":188,
"salary":123456
},
{
"name":"arjun",
"empId":142,
"salary":10000
},
{
"name":"aditya",
"empId":135,
"salary":9894
},
{
"name":"ravi",
"empId":175,
"salary":45893
}
]
  

f=open("demo.txt",'w')
for i in range(0,len(emp)):
    f.write("\n")
    for key,values in emp[i].items():      
        f.write(str(key + ":" + str(values)+","))
       
       


