class Developer:
    def __init__(self, company):
        self.company = company

    def work_at(self):
        print(f"Works at {self.company}.")

dev = Developer("Google")
print(dev.company)  # Access public variable
dev.work_at()       # Call public method