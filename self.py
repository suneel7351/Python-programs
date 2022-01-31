class car():

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def display(self):
        print("Model is", self.model)
        print("color is", self.color)


audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")

audi.display()
ferrari.display()
