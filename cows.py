#cows class that will return number of cows

class Cow:
    def __init__(self, number, guessed_number):
        self.number = number
        self.guessed_number = guessed_number
        self.cows_count = self.count()

    def __str__(self):
        return str(self.cows_count)

    def __repr__(self):
        return f'{self.number} ~ {self.guessed_number} = {self.cows_count}'

    def count(self):
        return sum(
            1 for digit1, digit2 in zip(list(str(self.number)), list(str(self.guessed_number))) if digit1 == digit2)

# cow = Cow(1234, 1267)
# print(cow)

#[(1,1),(2,2),(3,6),(4,7)]