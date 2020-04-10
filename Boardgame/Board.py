import random
from random import shuffle

from Boardgame.Card import Card
from Constants.Types import POOL, CONSTRUCTION, BIS, FENCE, REAL_ESTATE


class Board(object):

    def __init__(self, game):
        # self.state = State()
        self.game = game
        self.discards = []
        self.stacks = [[], [], []]
        self.currentCards = []
        self.prepare_board()
    
    def print_board(self):
        result = ""
        result += "First line:" + "\n"
        result += self.currentCards[0].front + self.stacks[0][0].back
        result += "Second line:" + "\n"
        result += self.currentCards[1].front + self.stacks[1][0].back
        result += "Third line:" + "\n"
        result += self.currentCards[2].front + self.stacks[2][0].back

        return "First line: " + "\n" + ""

    def get_card_stack_by_type(self, numbers, type):
        result = []
        for number in numbers:
            result.append(Card(number, type))
        return result

    def prepare_board(self):
        deck = []
        # On the board there are nine pools and there are nine cards with pools on them:
        # 3, 4, 6, 7, 8, 9, 10, 12, 13
        deck = deck + self.get_card_stack_by_type([3, 4, 6, 7, 8, 9, 10, 12, 13], POOL)
        # On the board there are eleven construction sites to mark off, however, there are only nine construction site cards (means you can only hit all eleven if you re-shuffle). The numers are:
        # 3, 4, 6, 7, 8, 9, 10, 12, 13
        deck = deck + self.get_card_stack_by_type([3, 4, 6, 7, 8, 9, 10, 12, 13], CONSTRUCTION)
        # There are nine BIS actions on the board and there are nine cards with BIS on the back, those number are:
        # 3, 4, 6, 7, 8, 9, 10, 12, 13
        deck = deck + self.get_card_stack_by_type([3, 4, 6, 7, 8, 9, 10, 12, 13], BIS)
        # There are thirty potential fence locations, there are eighteen fence cards, their numbers are:
        # 1, 2, 3, 5, 5, 6, 6, 7, 8, 8, 9, 10, 10, 11, 11, 13, 14, 15
        deck = deck + self.get_card_stack_by_type([1, 2, 3, 5, 5, 6, 6, 7, 8, 8, 9, 10, 10, 11, 11, 13, 14, 15], FENCE)
        # There are twelve parks you can fill in, there are eighteen cards with parks on them, their numbers are:
        # 1, 2, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9, 10, 11, 11, 12, 14, 15
        deck = deck + self.get_card_stack_by_type([1, 2, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9, 10, 11, 11, 12, 14, 15], FENCE)
        # There are eighteen real estate spots to mark on the board, there are eighteen real estate cards, their numbers are:
        # 1, 2, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9, 10, 11, 11, 12, 14, 15
        deck = deck + self.get_card_stack_by_type([1, 2, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9, 10, 11, 11, 12, 14, 15], REAL_ESTATE)

        # Now we have the deck, need to dive into 3 piles of 27 each
        random.shuffle(deck)
        self.stacks[0] = deck[0:26]
        self.stacks[1] = deck[27:53]
        self.stacks[2] = deck[54:80]

        # Now pop the first of each
        self.currentCards.append(self.stacks[0].pop())
        self.currentCards.append(self.stacks[1].pop())
        self.currentCards.append(self.stacks[2].pop())

        #TODO the goals