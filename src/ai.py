class AIData:
    def __init__(self, name, version, author, country):
        self.name = name
        self.version = version
        self.author = author
        self.country = country

    def __str__(self):
        return 'name="{}", version="{}", author="{}", country="{}"'.format(self.name, self.version, self.author, self.country)

class AI:
    def __init__(self):
        self.board_size = 0

    def set_board_size(self, board_size):
        self.board_size = board_size

    def get_data(self):
        return AIData("Unknown", "1.0", "Unknown", "FRA")

    def begin(self):
        pass

    def turn(self, x, y):
        pass

    def place(self, x, y):
        print('{},{}'.format(int(x), int(y)))

    def __str__(self):
        return str(self.get_data())