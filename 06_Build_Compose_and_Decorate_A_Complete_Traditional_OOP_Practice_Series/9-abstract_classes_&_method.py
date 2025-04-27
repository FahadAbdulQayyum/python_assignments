from abc import ABC, abstractmethod

class Student(ABC):
    @abstractmethod
    def info(self):
        pass

class New_Student(Student):
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def info(self):
        return f"""
        Name: {self.name}
        Roll#: {self.roll_no}
        """


fahad = New_Student("Fahad", "0032384")
print(fahad.info())