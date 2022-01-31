class Player:
    def __init__(self, name, run, role):
        self.name = name,
        self.run = run,
        self.role = role

    def display(self):
        print("Player name : ", self.name[0] +
              "\n" + "Run : ", str(self.run[0])+"\n" + "Role : " + self.role)


players = [Player("Kohali", 56, "Batsman"),
           Player("Dhoni", 99, "Batman"),
           Player("Rahul", 78, "Batman"),
           Player("Iyer", 76, "Batman"),
           Player("Pant", 12, "Batman"),
           Player("Rohit", 45, "Batman"),
           Player("Jadeja", 112, "Allrounder"),
           Player("Ashwin", 12, "Allrounder")
           ]

for i in players:
    print(i.display())
