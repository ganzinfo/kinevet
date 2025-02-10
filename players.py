import _global


class Players:
    def __init__(self):
        self.players = {}
        for i in range(_global.playercount):
            self.players[chr(i + 65)] = Player(i * 10)

    def playersPrintout(self):
        for i in range(_global.playercount):
            for j in range(4):
                print(self.players[chr(i + 65)].pieces['p' + str(j + 1)].piece['S'],
                      (self.players[chr(i + 65)].pieces['p' + str(j + 1)].piece['F']),
                      (self.players[chr(i + 65)].pieces['p' + str(j + 1)].piece['H']))

    def fullPrintout(self):
        # print(self.players['B'].pieces['p1'].piece)
        print(self.players)


class Player:
    def __init__(self, offset):
        self.pieces = {}
        self.name = ""
        self.ownCoordOnTableCs = {}
        self.tableCoordOnOwnCs = {}
        for i in range(4):
            self.pieces['p' + str(i + 1)] = Pieces()
        for i in range(40):
            # print (i+1,"  ",(40 + offset + i ) % 40+1)
            self.ownCoordOnTableCs[i + 1] = (40 + offset + i) % 40 + 1
            self.tableCoordOnOwnCs[(40 + offset + i) % 40 + 1] = i + 1

    def ownCoordOnTableCs(self, tableField):
        return self.ownCoordOnTableCs[tableField]

    def tableCoordsOnOwnCs(self, playerField):
        return self.tableCoordOnOwnCs(playerField)

    # def playerMoves(self, piece, count):
    #     # players.players['A'].pieces['p3'].piece['H']
    #     target = self.pieces[piece].piece['F'] + count
    #     if target > 40:
    #         pass# this.checkHouseFilling(target) #returns 1-4 for possible housefield or 0 if
    #
    #         print(self.houseFilling(target))
    #     else:
    #         self.pieces[piece].piece['F'] = target

    def checkPlayerWon(self):
        playerWon = True
        for i in range(4):
            if self.pieces['p' + str(i + 1)].piece['H'] == 0:
                playerWon = False
        return playerWon

    def checkPieceInStart(self, piece) -> bool:
        return self.pieces[piece].piece['S']

    def startPiece(self, count):
        pass

class Pieces:
    def __init__(self):
        self.piece = {}
        self.piece['S'] = True
        self.piece['F'] = 0
        self.piece['H'] = 0


# testing
players = Players()

# set player to winner
players.players['A'].pieces['p1'].piece['S'] = True
players.players['A'].pieces['p2'].piece['S'] = True
players.players['A'].pieces['p3'].piece['S'] = False
# players.players['A'].pieces['p4'].piece['S']= False
players.players['A'].pieces['p3'].piece['F'] = 38

# players.players['A'].pieces['p1'].piece['H'] = 1
# players.players['A'].pieces['p2'].piece['H'] = 2
# players.players['A'].pieces['p3'].piece['H'] = 3
# players.players['A'].pieces['p4'].piece['H']= 4
# players.playersPrintout()

# print(players.players['A'].playerWon())
# move a table class-ban és csak az eredmény jön át ide
# players.players['A'].playerMoves('p3',3)

# players.playersPrintout()
players.fullPrintout()
