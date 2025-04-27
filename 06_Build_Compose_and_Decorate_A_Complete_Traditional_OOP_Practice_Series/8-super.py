class Human:
    def __init__(self, name):
        self.name = name

class Teacher(Human):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t = Teacher("Raza", "Programming")
print(t.name, t.subject)  # Output: Alice Math