class Countdown:
    skills = ['cloud computing', 'langchain', 'openai', 'python', 'mongodb', 'expressjs', 'nodejs', 'react', 'javascript', 'css', 'html']

    def __init__(self):
        self.reversed_skills = self.skills[::-1]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.reversed_skills):
            skill = self.reversed_skills[self.index].capitalize()
            self.index += 1
            return skill
        else:
            raise StopIteration

for skill in Countdown():
    print(skill)