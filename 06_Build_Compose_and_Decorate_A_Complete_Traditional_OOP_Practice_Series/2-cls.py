class Speedometer:
    speed = 0

    def __init__(self):
        Speedometer.speed += 10

    @classmethod
    def get_speed(cls):
        return cls.speed

c1 = Speedometer()
c2 = Speedometer()
c3 = Speedometer()
print(f"{Speedometer.get_speed()}km/h.")