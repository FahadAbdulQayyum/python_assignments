class Analytics:
    @staticmethod
    def revenue(*args):
        print(args)
        sum = 0
        for a in args:
            sum += a
        return sum

print(Analytics.revenue(5, 7, 3))  # Output: 15