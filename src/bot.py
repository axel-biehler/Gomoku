from enum import Enum
from sys import stderr

class Owner(Enum):
    SELF = 1
    OPPONENT = 2
    NONE = 3

class Bot:
    def __init__(self, ai_class):
        self.is_running = True
        self.size = 0
        self.ai = ai_class(self)
        self.board = []

    def run(self):
        while self.is_running:
            self.loop()

    def loop(self):
        line = input()
        split = line.split()
        self.parse_command(split)

    def parse_command(self, split):
        command_map = {
            'START': self.start_cmd,
            'END': self.end_cmd,
            'ABOUT': self.about_cmd,
            'INFO': self.info_cmd,
            'BEGIN': self.begin_cmd,
            'TURN': self.turn_cmd,
            'BOARD': self.board_cmd,
        }
        command = split[0]

        try:
            command = command_map[command]
            args = split[1:]
            command(args)
        except KeyError: 
            print('Unknown command {}'.format(command), file=stderr)
            print('UNKNOWN')

    def init_board(self):
        self.board = [[Owner.NONE for _ in range(self.board_size)] for _ in range(self.board_size)]

    def start_cmd(self, args):
        self.board_size = int(args[0])
        self.init_board()
        print('OK')

    def end_cmd(self, args):
        self.is_running = False

    def about_cmd(self, args):
        print(str(self.ai))

    def info_cmd(self, args):
        pass

    def begin_cmd(self, args):
        self.ai.begin()

    def turn_cmd(self, args):
        x, y = list(map(lambda x: int(x), args[0].split(',')))
        self.board[x][y] = Owner.OPPONENT
        self.ai.turn(x, y)

    def board_cmd(self, args):
        line = input()
        x = 0
        y = 0
        self.init_board()
        while line != 'DONE':
            x, y, owner = list(map(lambda x: int(x), line.split(',')))
            self.board[x][y] = owner
            line = input()
        self.turn_cmd(['{},{}'.format(x, y)])

    def place(self, x, y):
        self.board[x][y] = Owner.SELF
        print('{},{}'.format(int(x), int(y)))
