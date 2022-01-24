from random import randrange
from sys import stderr

class Bot:
    def __init__(self, ai_class):
        self.is_running = True
        self.size = 0
        self.ai = ai_class()

    def run(self):
        while self.is_running:
            self.loop()

    def loop(self):
        line = input()
        split = line.split()
        self.parse_command(split)

    def parse_command(self, split):
        command_map = {
            'START': self.start,
            'END': self.end,
            'ABOUT': self.about,
            'INFO': self.info,
            'BEGIN': self.begin,
            'TURN': self.turn,
        }
        command = split[0]

        try:
            command = command_map[command]
            args = split[1:]
            command(args)
        except KeyError: 
            print('Unknown command {}'.format(command), file=stderr)
            print('UNKNOWN')

    def start(self, args):
        self.size = int(args[0])
        self.ai.set_board_size(self.size)
        print('OK')

    def end(self, args):
        self.is_running = False

    def about(self, args):
        print(str(self.ai))

    def info(self, args):
        pass

    def begin(self, args):
        self.ai.begin()

    def turn(self, args):
        pos_split = list(map(lambda x: int(x), args[0].split(',')))
        self.ai.turn(pos_split[0], pos_split[1])
