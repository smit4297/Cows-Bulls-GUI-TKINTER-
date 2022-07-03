#Bulls class that will return the number of bulls

class Bull:
    def __init__(self, number, guessed_number):
        self.number = number
        self.guessed_number = guessed_number
        self.bulls_count = self.count()

    def __str__(self):
        return str(self.bulls_count)

    def __repr__(self):
        return f'{self.number} ~ {self.guessed_number} = {self.bulls_count}'

    def count(self):
        number_list = list(str(self.number))
        guessed_number_list = list(str(self.guessed_number))
        bulls = 0
        for index in range(0, len(number_list)):
            if number_list[index] in guessed_number_list and number_list[index] != guessed_number_list[index]:
                bulls += 1
        return bulls
# bull = Bull(1234,2489)
# print(bull.count_bulls)
