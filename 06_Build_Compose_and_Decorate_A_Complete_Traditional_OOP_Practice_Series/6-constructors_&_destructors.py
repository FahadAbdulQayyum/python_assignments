class Life:
    def __init__(self):
        print("Life started...")

    def __del__(self):
        print("...life endeD")


life = Life()
del life