from random import shuffle

class Game(object):
    def __init__(self, cid):
        self.playerlist = {}
        self.cid = cid
        self.board = None

    def print_game(self):
        response = "No game!"
        if self.board is None:
            return response
        else:
            for 