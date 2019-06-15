class Person():
    def __init__(self):
        self.haircolor = ""
        self.personality = []
        self.birthday = ""
        self.name = ""
        self.age = ""
    def Greet(self):
        print(self.name,"says hi")
    def GetAge(self):
        return self.age
    def GetPersonality(self):
        return self.personality
    