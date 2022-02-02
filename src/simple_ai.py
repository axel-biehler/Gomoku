#!/usr/bin/env python3
from ai import AI, AIData
from bot import Owner

class SimpleAI(AI):
    def __init__(self, bot):
        super().__init__(bot)

    def get_data(self):
        return AIData("Simple AI", "1.0", "Alexandre Sauner", "FRA")

    def begin(self):
        middle = int(self.bot.board_size / 2)
        self.place(middle, middle)

    def turn(self, x, y):
        for yi in range(self.bot.board_size):
            for xi in range(self.bot.board_size):
                if self.board(xi, yi) == Owner.NONE:
                    self.place(xi, yi)
                    return