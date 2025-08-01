class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."


class Lion(Animal):
    def speak(self):
        return f"{self.name} the lion roars."


class Snake(Animal):
    def speak(self):
        return f"{self.name} the snake hisses."


zoo = [
    Lion("Simba"),
    Snake("Kaa"),
    Animal("GenericAnimal")
]

for animal in zoo:
    print(animal.speak())
