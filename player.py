# implementation of Players class
import _global


class Player:

    def __init__(self, symbol) -> None:


        self.player = {}
        self.var1 = None
        # self.pieces = {}
        # self.name = ""
        # for i in range(4):
        #     self.pieces[i+1]= (True,0,0)
        # self.player[symbol] = self.pieces
    # def playerPrintout(self):
    #     print(self.__str__())
    # def countStart(self,playerLetter):   #
    #     pass
#	def createPlayer(self, player):

    def ucoordToTable(self, userPos, player):  # User coordinate convert to table coordinate
        return (userPos + (ord(player) - 65) * 10) % 40

    def tcoordToUser(self, tablePos, player):  # Table coordinate convert to user coordinate
        return (tablePos - (ord(player) - 65) * 10) % 40

class HouseFields:

    def __init__(self, symbol):
        self.playerSymbol = ""
        self.houseFields = {}
        for i in range(4):
            self.houseFields[i + 1] = (0,)  # tuple first element is nr of piece
            self.playerSymbol = symbol

    def playerWon(self):
        playerWon = True
        for i in range(3):
            if self.houseFields[i + 1][0] == 0:
                playerWon = False
        return playerWon

class PlayFields:
    def __init__(self, symbol):
        self.playFields = {}
        for i in range(40):
            self.playFields[i + 1] = (0,)

class Startfields:
    def __init__(self):
        self.startField = 4