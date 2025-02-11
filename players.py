import _global


class Players:
    def __init__(self):
        self.player = {}
        for i in range(_global.playercount):
            self.player[chr(i + 65)] = Player(i * 10)

    def playersPrintout(self):
        for i in range(_global.playercount):
            for j in range(4):
                print(self.player[chr(i + 65)].piece['p' + str(j + 1)].posKey['S'],
                      (self.player[chr(i + 65)].piece['p' + str(j + 1)].posKey['F']),
                      (self.player[chr(i + 65)].piece['p' + str(j + 1)].posKey['H']))

    def fullPrintout(self):
        # print(self.player['B'].piece['p1'].posKey)
        print(self.player)


class Player:
    def __init__(self, offset):
        self.piece = {}
        self.name = ""
        self.ownCoordOnTableCs = {}
        self.tableCoordOnOwnCs = {}
        for i in range(4):
            self.piece['p' + str(i + 1)] = Pieces()
        for i in range(40):
            # print (i+1,"  ",(40 + offset + i ) % 40+1)
            self.ownCoordOnTableCs[i + 1] = (40 + offset + i) % 40 + 1
            self.tableCoordOnOwnCs[(40 + offset + i) % 40 + 1] = i + 1

    def ownCoordOnTableCs(self, tableField):
        return self.ownCoordOnTableCs[tableField]

    def tableCoordsOnOwnCs(self, playerField):
        return self.tableCoordOnOwnCs[playerField]

    # def playerMoves(self, posKey, count):
    #     # player.player['A'].piece['p3'].posKey['H']
    #     target = self.piece[posKey].posKey['F'] + count
    #     if target > 40:
    #         pass# this.checkHouseFilling(target) #returns 1-4 for possible housefield or 0 if
    #
    #         print(self.houseFilling(target))
    #     else:
    #         self.piece[posKey].posKey['F'] = target

    def checkPlayerWon(self):
        playerWon = True
        for i in range(4):
            if self.piece['p' + str(i + 1)].posKey['H'] == 0:
                playerWon = False
        return playerWon

    def checkPieceInStart(self, piece) -> bool:
        return self.piece[piece].posKey['S']

    def startPiece(self, count):
        pass

    def getPos(self, piece) -> ():
        piece = 'p' + str(piece)
        pos=self.piece[piece].posKey['pos']
        return (pos, self.piece[piece].posKey[pos])
        # sPos = self.piece[('p' + piece)].posKey['S']
        # hPos = self.piece[('p' + piece)].posKey['H']
        # fPos = self.piece[('p' + piece)].posKey['F']
        # if hPos != 0:
        #     retVal = ('h', hPos)
        # elif fPos != 0:
        #     retVal = ('f', fPos)
        # else:
        #     retVal = ('s',)


class Pieces:
    def __init__(self):
        self.posKey = {}
        self.posKey['pos'] = 'S'
        self.posKey['S'] = True
        self.posKey['F'] = 0
        self.posKey['H'] = 0
    def movePiece(self, steps):
        pass
        #TODO Adatszerkezetet megváltoztatni objektummezőkké
    """Csak a mozgást valósítja meg. Semmi vizsgálatot nem végez.
    Mozgás: -Startból steps a játékmezőkre
            -ha 40-nél nagyobb (saját KR), akkor egy ház töltő függvény jön"""

    def fillHouse(self,steps):
        pass

# # # testing
# players = Players()
# #
# # # set player to winner
# # players.player['A'].piece['p1'].posKey['S'] = True
# # players.player['A'].piece['p2'].posKey['S'] = True
# players.player['A'].piece['p3'].posKey['S'] = False
# # # player.player['A'].piece['p4'].posKey['S']= False
# players.player['A'].piece['p3'].posKey['F'] = 38
# players.player['A'].piece['p3'].posKey['pos'] = 'F'
# #
# # players.player['A'].piece['p1'].posKey['H'] = 1
# # players.player['A'].piece['p2'].posKey['H'] = 2
# # players.player['A'].piece['p3'].posKey['H'] = 3
# # players.player['A'].piece['p4'].posKey['H']= 4
# # # player.playersPrintout()
# #
# # print(players.player['A'].checkPlayerWon())
# # # move a table class-ban és csak az eredmény jön át ide
# # # player.player['A'].playerMoves('p3',3)
# #
# players.playersPrintout()
# # players.fullPrintout()
#
# print(players.player['A'].getPos(3))
