from random import randrange
import ai

class SimpleAI(ai.AI):
    def get_data(self):
        return ai.AIData("Simple AI", "1.0", "Alexandre Sauner", "FRA")

    def begin(self):
        middle = int(self.board_size / 2)
        self.place(middle, middle)

    def turn(self, x, y):
        self.place(x + 1, y)