from random import randint

class Dice:

    POSSIBLE_DICE_TYPE = (3, 4, 6, 8, 10, 12, 20, 100)

    def __init__(self, dice_type, number_of_rolls):
        if dice_type in Dice.POSSIBLE_DICE_TYPE:
            self.dice_type = dice_type
            self.number_of_rolls = number_of_rolls
        else:
            raise ValueError

    def roll(self):
        rollo = randint(1, self.dice_type)
        return rollo

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < self.number_of_rolls:
            self.counter += 1
            return self.roll()
        else:
            raise StopIteration

    def roll_the_dice(self, n):
        while (n > 0):
            yield self.roll()
            n -= 1


d1 = Dice(20, 5)

for roll in d1.roll_the_dice(10):
    print(roll)