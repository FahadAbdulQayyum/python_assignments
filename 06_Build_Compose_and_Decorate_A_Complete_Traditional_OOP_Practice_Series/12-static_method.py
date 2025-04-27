class CommaFormat:
    @staticmethod
    def commize(num):
        return "{:,}".format(num)

print(CommaFormat.commize(25000))