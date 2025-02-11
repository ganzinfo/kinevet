import _global
from players import Players

class Table:
    """ Table with 3 player, startposition:
    {'S': {'A': 4, 'B': 4, 'C': 4}, 'F': {1: ('', 0), 2: ('', 0), 3: ('', 0), 4: ('', 0), 5: ('', 0), 6: ('', 0), 7: ('', 0), 8: ('', 0), 9: ('', 0), 10: ('', 0), 11: ('', 0), 12: ('', 0), 13: ('', 0), 14: ('', 0), 15: ('', 0), 16: ('', 0), 17: ('', 0), 18: ('', 0), 19: ('', 0), 20: ('', 0), 21: ('', 0), 22: ('', 0), 23: ('', 0), 24: ('', 0), 25: ('', 0), 26: ('', 0), 27: ('', 0), 28: ('', 0), 29: ('', 0), 30: ('', 0), 31: ('', 0), 32: ('', 0), 33: ('', 0), 34: ('', 0), 35: ('', 0), 36: ('', 0), 37: ('', 0), 38: ('', 0), 39: ('', 0), 40: ('', 0)}, 'H': {'A': {1: (0,), 2: (0,), 3: (0,), 4: (0,)}, 'B': {1: (0,), 2: (0,), 3: (0,), 4: (0,)}, 'C': {1: (0,), 2: (0,), 3: (0,), 4: (0,)}}}

    """

    def __init__(self) -> None:
        # print("Table instantiated")
        # tabla letrehozasa
        # global g_table
        self.table = {}
        self.create_table()

    # print(g_table)
    # self.tablePrintout()

    def create_table(self):
        keyS = {}
        keyF = {}
        keyH = {}

        for i in range(_global.playercount):
            keyH_P = {}
            keyS[chr(i + 65)] = 4  # A-D, acc. to count player
            for j in range(4):
                keyH_P[j + 1] = (0,)
            keyH[chr(i + 65)] = keyH_P
        self.table["S"] = keyS
        for i in range(40):
            #special fields, knock off not possible, every first field per player
            if i % 10 == 0:
                keyF[i + 1] = ( '', True)
            else:
                keyF[i + 1] = ('', False)
        self.table["F"] = keyF
        self.table["H"] = keyH


    def tablePrintout(self):
        printout = "State of table\n"
        printout += "Startfields:\n"
        for key in self.table["S"]:
            printout += "("
            printout += key
            printout += ":"
            printout += str(self.table["S"][key])
            printout += ")"
        printout += "\nPlayfields:\n"
        count = 0
        for key in self.table["F"]:
            count += 1
            printout += "("
            printout += str(key)
            printout += ":"
            printout += str(self.table["F"][key][0])
            printout += ")"
            if count % 5 == 0:
                printout += "\n"
        printout += "House fields:\n"
        for key in self.table["H"]:
            printout += key
            printout += ":"
            printout += "("
            for key2 in self.table["H"][key]:
                printout += str(self.table["H"][key][key2][0])
                printout += ","
            printout += "\b)"
        print(printout)

    def fullPrintout(self):
        # print(self.table["S"], "\n", self.table["F"], "\n", self.table["H"])
        print(self.table)

    def movePiece(self, player, piece, steps):
        # players.player['A'].piece['p2'].posKey['S']
        pass
        print(players.player['A'].getPos(3))

    """
    lépés folyamata:
    kiválasztott bábu helyének lekérése a players.player['A'].piece['p2'].posKey['S'] vagy ['F'] ből
    Ha S-ben van, és 6-ot dobott, akkor saját 1-re kerül. Saját 1-et szintén a playerből lekérdezni, majd ... tisztázni...
    
    Ha F-ben van, akkor megvizsgálni, hogy az összeg > 40. Ha nem, simán lépés, ha igen, ház vizsgálat. 
    """
    # def checkMoveOwnpiece(self):
    #     pass
    #
    # def checkMoveOtherPiece(self):
    #     pass


# # testing
# table = Table()
# players = Players()
# #
# players.player['A'].piece['p1'].posKey['S'] = True
# players.player['A'].piece['p2'].posKey['S'] = True
# players.player['A'].piece['p3'].posKey['S'] = False
# players.player['A'].piece['p4'].posKey['S']= False
# players.player['A'].piece['p3'].posKey['F'] = 38
# #
# # players.player['A'].piece['p1'].posKey['H'] = 1
# # players.player['A'].piece['p2'].posKey['H'] = 2
# # players.player['A'].piece['p3'].posKey['H'] = 3
# # players.player['A'].piece['p4'].posKey['H']= 4
#
# table.tablePrintout()
#
#
#
#
#
# table.movePiece('A','3',5)
#
# # table.fullPrintout()
#
#
# # table.fullPrintout()
