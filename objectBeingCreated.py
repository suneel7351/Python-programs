

class Student:
    count = 0

    def __init__(self, name, rollNo):
        self.name = name,
        self.rollNo = rollNo
        Student.count += 1

    def display(self):
        print(self.name, self.rollNo)


obj1 = Student("suneel", 188)
obj2 = Student("aditya", 135)
obj3 = Student("arjun", 142)
obj4 = Student("ravi", 175)
obj5 = Student("shivam", 182)

print(Student.count)

