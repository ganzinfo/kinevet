# implementation of Players class
import _global


class Player:

    def __init__(self, symbol) -> None:
        # pass
        self.player = {}
        for i in range(4):
            self.player[(symbol, i + 1)] = (0)
    def playerPrintout(self):
        print(self.player)
    def countStart(self,playerLetter):   #
        pass
#	def createPlayer(self, player):
