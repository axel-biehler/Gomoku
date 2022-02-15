#!/usr/bin/env python3
from tkinter import HORIZONTAL
from turtle import screensize
from ai import AI, AIData
from bot import Owner
from enum import IntEnum

class alignment(IntEnum):
    SIZE = 0
    POS_X = 1
    POS_Y = 2
    DIRECTION = 3

class pieces(IntEnum):
    SCORE = 0
    POS_X = 1
    POS_Y = 2

class directions(IntEnum):
    HORIZONTAL = 0
    VERTICAL = 1
    DIAGONAL_DOWN = 2
    DIAGONAL_UP = 3

class BasicAi(AI):
    def __init__(self, bot):
        super().__init__(bot)

    def get_data(self):
        return AIData("Simple AI", "1.0", "Alexandre Sauner", "FRA")

    def begin(self):
        middle = int(self.bot.board_size / 2)
        self.place(middle, middle)

    def turn(self, x, y):
        move = self.find_diag_up();
        if (move != "Not efficient"):
            self.place(move[0], move[1])
            return
        move = self.find_diag_down();
        if (move != "Not efficient"):
            self.place(move[0], move[1])
            return
        move = self.find_horizontal();
        if (move != "Not efficient"):
            self.place(move[0], move[1])
            return
        move = self.find_vertical();
        if (move != "Not efficient"):
            self.place(move[0], move[1])
            return
        move = self.dumb_move()
        self.place(move[0], move[1])

    ## Picks a random place to start
    def dumb_move(self):
        for yi in range(self.bot.board_size - 1, 0, -1):
            for xi in range(self.bot.board_size - 1, 0, -1):
                if self.board(xi, yi) == Owner.NONE:
                    return (xi, yi)

    ## Find opportunities on horizontal axis
    def get_piece_horizontal(self, x, y):
        piece = [0, 0, 0, 0, 0]
        for i in range(5):
            piece[i] = self.board(x + i, y)
        score = 0
        for i in range(5):
            if (piece[i] == Owner.OPPONENT):
                return 0
            elif (piece[i] == Owner.SELF):
                score += 1
        return score

    def horizontal_placement(self, best_piece):
        piece = [0, 0, 0, 0, 0]
        for i in range(5):
            piece[i] = self.board(best_piece[pieces.POS_X] + i, best_piece[pieces.POS_Y])
        for i in range(5):
            if (piece[i] == Owner.NONE):
                return (best_piece[pieces.POS_X] + i, best_piece[pieces.POS_Y])

    def find_horizontal(self):
        best_piece = [0, 0, 0]
        for yi in range(self.bot.board_size):
            for xi in range(self.bot.board_size - 4):
                score = self.get_piece_horizontal(xi, yi)
                if (best_piece[pieces.SCORE] < score):
                    best_piece[pieces.SCORE] = score
                    best_piece[pieces.POS_X] = xi
                    best_piece[pieces.POS_Y] = yi
        if (best_piece[pieces.SCORE] == 0):
            return "Not efficient"
        return self.horizontal_placement(best_piece)
    
    ## Find opportunities on vertical axis
    def get_piece_vertical(self, x, y):
        piece = [0, 0, 0, 0, 0]
        for i in range(5):
            piece[i] = self.board(x, y + i)
        score = 0
        for i in range(5):
            if (piece[i] == Owner.OPPONENT):
                return 0
            elif (piece[i] == Owner.SELF):
                score += 1
        return score

    def vertical_placement(self, best_piece):
        piece = [0, 0, 0, 0, 0]
        for i in range(5):
            piece[i] = self.board(best_piece[pieces.POS_X], best_piece[pieces.POS_Y] + i)
        for i in range(5):
            if (piece[i] == Owner.NONE):
                return (best_piece[pieces.POS_X], best_piece[pieces.POS_Y] + i)

    def find_vertical(self):
        best_piece = [0, 0, 0]
        for yi in range(self.bot.board_size - 4):
            for xi in range(self.bot.board_size):
                score = self.get_piece_vertical(xi, yi)
                if (best_piece[pieces.SCORE] < score):
                    best_piece[pieces.SCORE] = score
                    best_piece[pieces.POS_X] = xi
                    best_piece[pieces.POS_Y] = yi
        if (best_piece[pieces.SCORE] == 0):
            return "Not efficient"
        return self.vertical_placement(best_piece)

    ## Find opportunities on descending diagonal axis
    def get_piece_diag_down(self, x, y):
        piece = [0, 0, 0, 0, 0]
        for i in range(5):
            piece[i] = self.board(x + i, y + i)
        score = 0
        for i in range(5):
            if (piece[i] == Owner.OPPONENT):
                return 0
            elif (piece[i] == Owner.SELF):
                score += 1
        return score

    def diag_down_placement(self, best_piece):
        piece = [0, 0, 0, 0, 0]
        for i in range(5):
            piece[i] = self.board(best_piece[pieces.POS_X] + i, best_piece[pieces.POS_Y] + i)
        for i in range(5):
            if (piece[i] == Owner.NONE):
                return (best_piece[pieces.POS_X] + i, best_piece[pieces.POS_Y] + i)

    def find_diag_down(self):
        best_piece = [0, 0, 0]
        for yi in range(self.bot.board_size - 4):
            for xi in range(self.bot.board_size - 4):
                score = self.get_piece_diag_down(xi, yi)
                if (best_piece[pieces.SCORE] < score):
                    best_piece[pieces.SCORE] = score
                    best_piece[pieces.POS_X] = xi
                    best_piece[pieces.POS_Y] = yi
        if (best_piece[pieces.SCORE] == 0):
            return "Not efficient"
        return self.diag_down_placement(best_piece)

    ## Find opportunities on upward diagonal axis
    def get_piece_diag_up(self, x, y):
        piece = [0, 0, 0, 0, 0]
        for i in range(5):
            piece[i] = self.board(x + i, y - i)
        score = 0
        for i in range(5):
            if (piece[i] == Owner.OPPONENT):
                return 0
            elif (piece[i] == Owner.SELF):
                score += 1
        return score

    def diag_up_placement(self, best_piece):
        piece = [0, 0, 0, 0, 0]
        for i in range(5):
            piece[i] = self.board(best_piece[pieces.POS_X] + i, best_piece[pieces.POS_Y] - i)
        for i in range(5):
            if (piece[i] == Owner.NONE):
                return (best_piece[pieces.POS_X] + i, best_piece[pieces.POS_Y] - i)

    def find_diag_up(self):
        best_piece = [0, 0, 0]
        for yi in range(4, self.bot.board_size - 4):
            for xi in range(self.bot.board_size - 4):
                score = self.get_piece_diag_up(xi, yi)
                if (best_piece[pieces.SCORE] < score):
                    best_piece[pieces.SCORE] = score
                    best_piece[pieces.POS_X] = xi
                    best_piece[pieces.POS_Y] = yi
        if (best_piece[pieces.SCORE] == 0):
            return "Not efficient"
        return self.diag_up_placement(best_piece)
