f = open("demo.txt", 'a')


class Employee:
    def __init__(self, name, EmpId, role, salary):
        self.name = name,


class Engineer(Employee):
    def display(self):
        f.write(str(self.name[0]))


class Manager(Employee):
    def display(self):
        f.write(str(self.name[0]))


class Worker(Employee):
    def display(self):
        f.write(str(self.name[0]))


obj1 = Manager("ramesh", 122, "manager", 123456)
obj2 = Engineer("suresh", 124, "Engineer", 231456)
obj3 = Worker("rahul", 199, "worker", 34000)
obj1.display()
obj2.display()
obj3.display()
# file = open("record.txt", 'a')
# data1 = str("name: "+obj1.display()
#             ['name'][0]+"\n"+"Empid: "+str(obj1.display()['EmpId'][0])+"\n"+"Salary: "+str(obj1.display()['Salary'])+"\n"+"Role: "+obj1.display()['Role'][0])
# data2 = str("name: "+obj1.display()
#             ['name'][0]+"\n"+"Empid: "+str(obj1.display()['EmpId'][0])+"\n"+"Salary: "+str(obj1.display()['Salary'])+"\n"+"Role: "+obj1.display()['Role'][0])
# data3 = str("name: "+obj1.display()
#             ['name'][0]+"\n"+"Empid: "+str(obj1.display()['EmpId'][0])+"\n"+"Salary: "+str(obj1.display()['Salary'])+"\n"+"Role: "+obj1.display()['Role'][0])

# file.write(data1)
# file.write("\n" + data2 + "\n")
# file.write(data3)
# f = open("record.txt", "r")
# print(f.read())
