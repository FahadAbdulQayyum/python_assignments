class Developer:
    def __init__(self, name, experience):
        self.name = name
        self.experince = experience
    
    def display(self):
        print(f"""
Name: {self.name}
Experience: {self.experince
        }""")
    
dev = Developer("Fahad", 3.5)
dev.display()