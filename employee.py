class Employee:
    def __init__(self, name, EmpId, role, salary):
        self.name = name,
        self.EmpId = EmpId,
        self.role = role,
        self.salary = salary


class Engineer(Employee):
    def display(self):

        print("The employee name is : ",
              self.name[0] + "\n"
              + "EmployeeId : ", str(self.EmpId[0]) + "\n" + "role : ", self.role[0]+"\n"+"Salar : ", self.salary)


class Manager(Employee):
    def display(self):

        print("The employee name is : ",
              self.name[0] + "\n"
              + "EmployeeId : ", str(self.EmpId[0]) + "\n" + "role : ", self.role[0]+"\n"+"Salar : ", self.salary)


class Worker(Employee):
    def display(self):

        print("The employee name is : ",
              self.name[0] + "\n"
              + "EmployeeId : ", str(self.EmpId[0]) + "\n" + "role : ", self.role[0]+"\n"+"Salar : ", self.salary)


obj1 = Manager("ramesh", 122, "manager", 123456)
obj2 = Engineer("suresh", 124, "Engineer", 231456)
obj3 = Worker("rahul", 199, "worker", 34000)
obj1.display()
obj2.display()
obj3.display()
