class Hero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def name(self):
        return self.name

miya = Hero("Miya", 20)
print(miya.name)