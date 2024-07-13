class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color
    def fly(self):
        print(f"{self.name} fly")
    def eat(self):
        print(f"{self.name} eat")
    def sing(self):
        print(f"{self.name} sing {self.voice}")
    def info(self):
        print(f"Name: {self.name}, Voice: {self.voice}, Color: {self.color}")
class Pigeon(Bird):
    def __init__(self, name, voice, color,favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food=favorite_food
    def walk(self):
        print(f"{self.name} walk")

bird1=Pigeon("Gosha","Curlyk","Grey","bread")
bird1.sing()
bird1.info()
bird1.walk()