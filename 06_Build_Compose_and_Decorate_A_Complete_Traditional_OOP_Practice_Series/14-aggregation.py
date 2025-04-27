class Developer:
    def __init__(self, name):
        self.name = name

class Skill:
    def __init__(self, name):
        self.name = name
        self.employee = None

    def assign_project(self, project):
        self.project = project

dev = Developer("Fahad")
skill = Skill("AI")
skill.assign_project(dev)
print(skill.project.name)