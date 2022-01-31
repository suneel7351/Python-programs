class Employee:

    def __init__(self, name, empId, salary):
        self.name = name
        self.empId = empId
        self.salary = salary

    def display(self):
        print("The name of the employee is :" + self.name+", Employee Id :" +
              str(self.empId)+", and salary of employee is :"+str(self.salary))


Emp1 = Employee("ramesh", 121, 123423)
Emp2 = Employee("mahesh", 334, 78956)
Emp3 = Employee("suresh", 249, 43532)
Emp4 = Employee("mohan", 542, 4500)
Emp5 = Employee("ram", 347, 8900)
Emp1.display()
Emp2.display()
Emp3.display()
Emp4.display()
Emp5.display()
