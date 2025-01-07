# impementation of class Table
# dictionary szintek
# 1: 3 key-value: [S]:2 or 3 or 4 values, [F] 1-40 fields, [H] 2 or 3 or 4 houses
# values: diectionaries:
# [S]: keys:[A]...[D], values: int count of pieces in start per player
# [F]: keys:[1]...[40], values:  tuple:(piece on field: 'A3', special property of field, True-False or int 0,1,2 etc.)
# [H]: keys: [A]...[D], values: tuple: (piece on field: 3)


import _global


class Table:
    def __init__(self) -> None:
        # print("Table instantiated")
        # tabla letrehozasa
        # global g_table
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
                keyH_P[j+1] = (False,)
            keyH[chr(i + 65)] = keyH_P
        _global.table["S"] = keyS
        for i in range(40):
            keyF[i+1]= ('',0)
        _global.table["F"] = keyF
        _global.table["H"] = keyH

    def tablePrintout(self):
        count = 0
        printout = "A tábla:\n"
        for key in _global.table:
            match key[0]:
                case "S":
                    printout += "("
                    printout += key[0]
                    printout += key[1]
                    printout += ":"
                    printout += str(_global.table[key][0])
                    printout += ")"
                case "F":
                    printout += "("
                    printout += key[0]
                    printout += str(key[1])
                    printout += ":"
                    printout += str(_global.table[key][0])
                    # printout += str(_global.table[key][1])
                    printout += ")"
                case "H":
                    printout += "("
                    printout += key[0]
                    printout += key[1]
                    printout += str(key[2])
                    printout += ":"
                    printout += str(_global.table[key][0])
                    printout += ")"
            count += 1
            # soremelesek beszurasa kiiras formazahoz
            limit = _global.playercount + 40
            if count == _global.playercount:
                printout += "\n\n"
            if count > _global.playercount and count < limit and (count - _global.playercount) % 5 == 0:
                printout += "\n"
            if count == limit:
                printout += "\n\n"
            if count > limit and (count - limit) % 4 == 0:
                printout += "\n"
        print(printout)

    def fullPrintout(self):
        print(_global.table["S"],"\n",_global.table["F"],"\n",_global.table["H"])

    def movePiece(self, player, piece, places):
        # a startból indulás itt valósul meg, nem a for - case-ben. 0-s bábuval lépés.
        # start = ()
        for key in _global.table:
            match key[0]:
                case "F":
                    if _global.table[key][0] == player + str(piece):
                        print("found", (player + str(piece)))
                        # start = key[0]+str(key[1])
                        pass
                case "H":
                    if _global.table[key][0] == player + str(piece):
                        pass

                case _:
                    # A babu a startban van
                    if player == key[1]:
                        # ezt az egészet egy függvénybe???
                        targetKey = ('F', places)
                        # ('',0,0)
                        # print(_global.table[key])
                        newTuple = (player + str(piece), _global.table[targetKey][1], _global.table[targetKey][2])
                        _global.table[targetKey] = newTuple

                        # startból kivonni egyet
                        targetKey = ('S', player)
                        # print(_global.table[targetKey][0])
                        _global.table[targetKey][0] -= 1

    def checkWinner(self):
        pass
