class Player:
    def __init__(self, symbol, moves, score):
        self.symbol = symbol
        self.score = score
        self.moves = moves
        self.is_a_computer = False