class Program:
    def start(self):
        return "Development started"

class Student:
    def __init__(self, program):
        self.program = program

    def start(self):
        return self.program.start()

program = Program()
student = Student(program)
print(student.start())