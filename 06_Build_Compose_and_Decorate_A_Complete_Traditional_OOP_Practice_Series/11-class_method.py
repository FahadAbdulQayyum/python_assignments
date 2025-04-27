class Run:
    pace = 0

    @classmethod
    def run_faster(cls):
        cls.pace += 10

Run.run_faster()
print(Run.pace)