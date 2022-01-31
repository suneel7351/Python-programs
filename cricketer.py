class Cricketer:
    def __init__(self, name, height, role, battingStyle, bowlingStyle, run):
        self.name = name,
        self.height = height,
        self.role = role,
        self.battingStyle = battingStyle,
        self.bowlingStyle = bowlingStyle,
        self.run = run

    def display(self):
        print("Name : " + (self.name)[0]
              + "\n" + "Height : " + str((self.height)[0])
              + "\n" + "Role : " + (self.role)[0]
              + "\n" + "Batting Style : " +
              (self.battingStyle)[0]
              + "\n" + "Bowling style : " + (self.bowlingStyle)[0]
              + "\n" + "Run : " + str(self.run))


player = [
    Cricketer("Rahul", 5.9, "Batsman wicketKeeper",
              "righthand", "right handmedium pace", 2344),
    Cricketer("kohali", 5.8, "Batsman",
              "righthand", "right handmedium pace", 12344),
    Cricketer("Rohit", 5.9, "Batsman",
              "righthand", "off spin", 8990),
    Cricketer("dhoni", 6, "Batsman wicketKeeper",
              "righthand", "right handmedium pace", 12000)
]

for x in player:
    print(x.display())
