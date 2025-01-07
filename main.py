import _global
#from player import Player
from table import Table
from player import Player

_global.playercount = 3
# playerek létrehozása
# player1 = Player("A")
# player1.playerPrintout()

# players = {}
# for i in range(_global.playercount):
# 	players[chr(i + 65)]=(Player(chr(i + 65)))
# # print(players["A"])
# # print(players["B"])
# # print(players["C"])
# print(players["A"].playerPrintout())
# print(players["B"].playerPrintout())
# print(players["C"].playerPrintout())

# table szakasz
table1 = Table()
# table1.tablePrintout()
table1.fullPrintout()





# # Table and user pos convert to each other
# print(table1.ucoordToTable(26,"A"))
# print(table1.ucoordToTable(26,"B"))
# print(table1.ucoordToTable(26,"C"))
# print(table1.ucoordToTable(26,"D"))
#
# print(table1.tcoordToUser(16,"A"))
# print(table1.tcoordToUser(16,"B"))
# print(table1.tcoordToUser(16,"C"))
# print(table1.tcoordToUser(16,"D"))

# # test if someone has won
# pieceTup = (True,)
# player = "A"
# _global.table["H"][player][1] = pieceTup
# _global.table["H"][player][2] = pieceTup
# _global.table["H"][player][3] = pieceTup
# _global.table["H"][player][4] = pieceTup
# print(table1.checkWinner("A"))

# table1.movePiece("A",1,6)
# table1.movePiece("A",2,5)
# table1.movePiece("A",3,4)
# # # table1.movePiece("A",1,4)
# # # table1.movePiece("A",1,2)
# # table1.movePiece("A",1,1)
# # #table1.fullPrintout()
# table1.tablePrintout()
"""
import proto1

#print(proto1.Table().create_table())


game1 = proto1.Game()

#print(game1.fomenu())

"""
