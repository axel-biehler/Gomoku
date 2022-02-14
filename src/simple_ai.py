#!/usr/bin/env python3
from tkinter import HORIZONTAL
from ai import AI, AIData
from bot import Owner
from enum import Enum

class alignment(Enum):
    SIZE = 0
    POS_X = 1
    POS_Y = 2
    DIRECTION = 3

class directions(Enum):
    HORIZONTAL = 0
    VERTICAL = 1
    DIAGONAL_DOWN = 2
    DIAGONAL_UP = 3

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

    def find_horizontal(self):
        aligned = 0
        biggest = (0, 0, 0, 0);
        for xi in range(self.bot.board_size):
            for yi in range(self.bot.board_size):
                if self.board(xi, yi) == Owner.SELF:
                    aligned += 1
                elif self.board(xi, yi) == Owner.NONE:
                    if biggest[alignment.SIZE] < aligned:
                        biggest = (aligned, xi, yi, directions.HORIZONTAL)
                    aligned = 0
                elif self.board(xi, yi) == Owner.OPPONENT:
                    aligned = 0
        return biggest