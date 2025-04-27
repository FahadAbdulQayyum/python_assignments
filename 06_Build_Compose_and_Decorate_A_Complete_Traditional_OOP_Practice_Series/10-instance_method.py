class Human:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language

    def speak(self):
        print(f"{self.name} speaks {self.language}!")

human = Human("Fahad", 27, "Balochi")
human.speak()