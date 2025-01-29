# impementation of class Table
# dictionary szintek
# 1: 3 key-value: [S]:2 or 3 or 4 values, [F] 1-40 fields, [H] 2 or 3 or 4 houses
# values: diectionaries:
# [S]: keys:[A]...[D], values: int count of pieces in start per player
# [F]: keys:[1]...[40], values:  tuple:(piece on field: 'A3', special property of field, True-False or int 0,1,2 etc.)
# [H]: keys: [A]...[D], values: tuple: (piece on field: 3)


import _global


class Table:
    """ Table with 3 players, startposition:
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
            keyS[chr(i + 65)] = 4  # A-D, acc. to count players
            for j in range(4):
                keyH_P[j + 1] = (0,)
            keyH[chr(i + 65)] = keyH_P
        self.table["S"] = keyS
        for i in range(40):
            keyF[i + 1] = ('', 0)
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
            count +=1
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
        #print(self.table["S"], "\n", self.table["F"], "\n", self.table["H"])
        print(self.table)

    def movePiece(self, player, piece, places):
        pass





#testing
table = Table()
#
# table.tablePrintout()
table.fullPrintout()
table.fullPrintout()