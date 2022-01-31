class Parent:
    def __init__(self, name, salary):
        pass


class Child(Parent):
    def __init__(self, name, salary, role):
        super().__init__(name, salary)
        self.role = role
        self.name = name,
        self.salary = salary

    def display(self):
        print(self.name[0], self.salary, self.role)


obj = Child("Suneel", 234123, "Engineer")
obj.display()
