try:
    class Student:

        def __init__(self, name, rollNo):
            self.name = name
            self.rollNo = rollNo

        def display(self):
            print(self.name, self.rollNo)

    obj = Student("suneel", 188)
    x = (input("Enter something : "))

    obj.dataMember = x
    if obj.dataMember:
        raise Exception("Can't create data member")
    else:
        print(obj.display())


except Exception():
    pass
