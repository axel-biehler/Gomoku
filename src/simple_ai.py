#!/usr/bin/env python3
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

class SimpleAI(AI):
    def __init__(self, bot):
        super().__init__(bot)

    def get_data(self):
        return AIData("Simple AI", "1.0", "Alexandre Sauner", "FRA")

    def begin(self):
        middle = int(self.bot.board_size / 2)
        self.place(middle, middle)

    def turn(self, x, y):
        off_moves = list()
        off_moves.append(self.find_diag_up())
        off_moves.append(self.find_diag_down())
        off_moves.append(self.find_horizontal())
        off_moves.append(self.find_vertical())
        def_moves = list()
        def_moves.append(self.defend_diag_up())
        def_moves.append(self.defend_diag_down())
        def_moves.append(self.defend_horizontal())
        def_moves.append(self.defend_vertical())

        best_def = [0, 0, 0]
        for move in def_moves:
            if (best_def[2] < move[2] and int(2) < move[2]):
                best_def = move
        if (best_def[2] > 0):
            self.place(best_def[0], best_def[1])
            return

        best_off = [0, 0, 0]
        for move in off_moves:
            if (best_off[2] < move[2]):
                best_off = move
        if (best_off[2] > 0):
            self.place(best_off[0], best_off[1])
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
                return (best_piece[pieces.POS_X] + i, best_piece[pieces.POS_Y], best_piece[pieces.SCORE])

    def find_horizontal(self):
        best_piece = [0, 0, 0]
        for yi in range(self.bot.board_size):
            for xi in range(self.bot.board_size - 4):
                score = self.get_piece_horizontal(xi, yi)
                if (best_piece[pieces.SCORE] < score):
                    best_piece[pieces.SCORE] = score
                    best_piece[pieces.POS_X] = xi
                    best_piece[pieces.POS_Y] = yi
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
                return (best_piece[pieces.POS_X], best_piece[pieces.POS_Y] + i, best_piece[pieces.SCORE])

    def find_vertical(self):
        best_piece = [0, 0, 0]
        for yi in range(self.bot.board_size - 4):
            for xi in range(self.bot.board_size):
                score = self.get_piece_vertical(xi, yi)
                if (best_piece[pieces.SCORE] < score):
                    best_piece[pieces.SCORE] = score
                    best_piece[pieces.POS_X] = xi
                    best_piece[pieces.POS_Y] = yi
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
                return (best_piece[pieces.POS_X] + i, best_piece[pieces.POS_Y] + i, best_piece[pieces.SCORE])

    def find_diag_down(self):
        best_piece = [0, 0, 0]
        for yi in range(self.bot.board_size - 4):
            for xi in range(self.bot.board_size - 4):
                score = self.get_piece_diag_down(xi, yi)
                if (best_piece[pieces.SCORE] < score):
                    best_piece[pieces.SCORE] = score
                    best_piece[pieces.POS_X] = xi
                    best_piece[pieces.POS_Y] = yi
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
                return (best_piece[pieces.POS_X] + i, best_piece[pieces.POS_Y] - i, best_piece[pieces.SCORE])

    def find_diag_up(self):
        best_piece = [0, 0, 0]
        for yi in range(4, self.bot.board_size):
            for xi in range(self.bot.board_size - 4):
                score = self.get_piece_diag_up(xi, yi)
                if (best_piece[pieces.SCORE] < score):
                    best_piece[pieces.SCORE] = score
                    best_piece[pieces.POS_X] = xi
                    best_piece[pieces.POS_Y] = yi
        return self.diag_up_placement(best_piece)


## DEFENSE


    ## Find where to block on horizontal axis
    def def_get_piece_horizontal(self, x, y):
        piece = [0, 0, 0, 0, 0]
        for i in range(5):
            piece[i] = self.board(x + i, y)
        score = 0
        for i in range(5):
            if (piece[i] == Owner.SELF):
                return 0
            elif (piece[i] == Owner.OPPONENT):
                score += 1
        return score

    def horizontal_blocking(self, best_piece):
        piece = [0, 0, 0, 0, 0]
        for i in range(5):
            piece[i] = self.board(best_piece[pieces.POS_X] + i, best_piece[pieces.POS_Y])
        for i in range(5):
            if (piece[i] == Owner.NONE):
                return (best_piece[pieces.POS_X] + i, best_piece[pieces.POS_Y], best_piece[pieces.SCORE])

    def defend_horizontal(self):
        best_piece = [0, 0, 0]
        for yi in range(self.bot.board_size):
            for xi in range(self.bot.board_size - 4):
                score = self.def_get_piece_horizontal(xi, yi)
                if (best_piece[pieces.SCORE] < score):
                    best_piece[pieces.SCORE] = score
                    best_piece[pieces.POS_X] = xi
                    best_piece[pieces.POS_Y] = yi
        return self.horizontal_blocking(best_piece)
    
    ## Find where to block on vertical axis
    def def_get_piece_vertical(self, x, y):
        piece = [0, 0, 0, 0, 0]
        for i in range(5):
            piece[i] = self.board(x, y + i)
        score = 0
        for i in range(5):
            if (piece[i] == Owner.SELF):
                return 0
            elif (piece[i] == Owner.OPPONENT):
                score += 1
        return score

    def vertical_blocking(self, best_piece):
        piece = [0, 0, 0, 0, 0]
        for i in range(5):
            piece[i] = self.board(best_piece[pieces.POS_X], best_piece[pieces.POS_Y] + i)
        for i in range(5):
            if (piece[i] == Owner.NONE):
                return (best_piece[pieces.POS_X], best_piece[pieces.POS_Y] + i, best_piece[pieces.SCORE])

    def defend_vertical(self):
        best_piece = [0, 0, 0]
        for yi in range(self.bot.board_size - 4):
            for xi in range(self.bot.board_size):
                score = self.def_get_piece_vertical(xi, yi)
                if (best_piece[pieces.SCORE] < score):
                    best_piece[pieces.SCORE] = score
                    best_piece[pieces.POS_X] = xi
                    best_piece[pieces.POS_Y] = yi
        return self.vertical_blocking(best_piece)

    ## Find where to block on descending diagonal axis
    def def_get_piece_diag_down(self, x, y):
        piece = [0, 0, 0, 0, 0]
        for i in range(5):
            piece[i] = self.board(x + i, y + i)
        score = 0
        for i in range(5):
            if (piece[i] == Owner.SELF):
                return 0
            elif (piece[i] == Owner.OPPONENT):
                score += 1
        return score

    def diag_down_blocking(self, best_piece):
        piece = [0, 0, 0, 0, 0]
        for i in range(5):
            piece[i] = self.board(best_piece[pieces.POS_X] + i, best_piece[pieces.POS_Y] + i)
        for i in range(5):
            if (piece[i] == Owner.NONE):
                return (best_piece[pieces.POS_X] + i, best_piece[pieces.POS_Y] + i, best_piece[pieces.SCORE])

    def defend_diag_down(self):
        best_piece = [0, 0, 0]
        for yi in range(self.bot.board_size - 4):
            for xi in range(self.bot.board_size - 4):
                score = self.def_get_piece_diag_down(xi, yi)
                if (best_piece[pieces.SCORE] < score):
                    best_piece[pieces.SCORE] = score
                    best_piece[pieces.POS_X] = xi
                    best_piece[pieces.POS_Y] = yi
        return self.diag_down_blocking(best_piece)

    ## Find where to block on upward diagonal axis
    def def_get_piece_diag_up(self, x, y):
        piece = [0, 0, 0, 0, 0]
        for i in range(5):
            piece[i] = self.board(x + i, y - i)
        score = 0
        for i in range(5):
            if (piece[i] == Owner.SELF):
                return 0
            elif (piece[i] == Owner.OPPONENT):
                score += 1
        return score

    def diag_up_blocking(self, best_piece):
        piece = [0, 0, 0, 0, 0]
        for i in range(5):
            piece[i] = self.board(best_piece[pieces.POS_X] + i, best_piece[pieces.POS_Y] - i)
        for i in range(5):
            if (piece[i] == Owner.NONE):
                return (best_piece[pieces.POS_X] + i, best_piece[pieces.POS_Y] - i, best_piece[pieces.SCORE])

    def defend_diag_up(self):
        best_piece = [0, 0, 0]
        for yi in range(4, self.bot.board_size):
            for xi in range(self.bot.board_size - 4):
                score = self.def_get_piece_diag_up(xi, yi)
                if (best_piece[pieces.SCORE] < score):
                    best_piece[pieces.SCORE] = score
                    best_piece[pieces.POS_X] = xi
                    best_piece[pieces.POS_Y] = yi
        return self.diag_up_blocking(best_piece)
