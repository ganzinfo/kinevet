# implementation of Players class
import _global


class Player:

    def __init__(self, symbol) -> None:
        pass
    def playerPrintout(self):
        print(self.__str__())
    def countStart(self,playerLetter):   #
        pass
#	def createPlayer(self, player):

    def ucoordToTable(self, userPos, player):  # User coordinate convert to table coordinate
        return (userPos + (ord(player) - 65) * 10) % 40

    def tcoordToUser(self, tablePos, player):  # Table coordinate convert to user coordinate
        return (tablePos - (ord(player) - 65) * 10) % 40