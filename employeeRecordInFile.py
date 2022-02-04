class Employee:
    def __init__(self, name, EmpId, role, salary):
        self.name = name,
        self.EmpId = EmpId,
        self.role = role,
        self.salary = salary


class Engineer(Employee):
    def display(self):

        return {"name": self.name, "EmpId": self.EmpId, "Salary": self.salary, "Role": self.role}


class Manager(Employee):
    def display(self):

        return {"name": self.name, "EmpId": self.EmpId, "Salary": self.salary, "Role": self.role}


class Worker(Employee):
    def display(self):

        return {"name": self.name, "EmpId": self.EmpId, "Salary": self.salary, "Role": self.role}


obj1 = Manager("ramesh", 122, "manager", 123456)
obj2 = Engineer("suresh", 124, "Engineer", 231456)
obj3 = Worker("rahul", 199, "worker", 34000)
file = open("record.txt", 'a')
data1 = str("name: "+obj1.display()
            ['name'][0]+"\n"+"Empid: "+str(obj1.display()['EmpId'][0])+"\n"+"Salary: "+str(obj1.display()['Salary'])+"\n"+"Role: "+obj1.display()['Role'][0])
data2 = str("name: "+obj1.display()
            ['name'][0]+"\n"+"Empid: "+str(obj1.display()['EmpId'][0])+"\n"+"Salary: "+str(obj1.display()['Salary'])+"\n"+"Role: "+obj1.display()['Role'][0])
data3 = str("name: "+obj1.display()
            ['name'][0]+"\n"+"Empid: "+str(obj1.display()['EmpId'][0])+"\n"+"Salary: "+str(obj1.display()['Salary'])+"\n"+"Role: "+obj1.display()['Role'][0])

file.write(data1)
file.write("\n" + data2 + "\n")
file.write(data3)
f = open("record.txt", "r")
print(f.read())
