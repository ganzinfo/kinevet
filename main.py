import random
import sys
#import keyboard
import _global
from table import Table
from players import Players


def inputPlayercount() -> None:
	playercountOk = False
	while not playercountOk:
		val = input("Number of player (2-4, q = quit ):")
		try:
			val = int(val)
			if val > 1 and val < 5:
				_global.playercount = val
				playercountOk = True
		except ValueError:
			if val == "q":
				print("Quit game... Bye.")
				sys.exit()

players = Players()

def inputPlayersNames():
	for i in range(_global.playercount):
		pass
#start
print("\tWelcome to Ludo game.\n\tHow many player will play?")
# Number of players:
inputPlayercount()			# in release
# _global.playercount = 4		# development step


#print (_global.playercount)
#Initializing the game
#print("Initializing...")


print(_global.keysToListen["selectPiece"])

sys.exit()

table = Table()			# in release
# table.fullPrintout()
table.tablePrintout()	# test step

# playerek létrehozása _global
for i in range(_global.playercount):		# in release
	_global.players[chr(i + 65)]=(Player(chr(i + 65)))		# in release
	_global.players[chr(i + 65)].name = input("Enter the %s. player name:" % (i + 1))
	#print(_global.player[chr(i + 65)].name)	# test step
# print(_global.player)				# test steps
# print(_global.player["A"].player)	# test steps
# print(_global.player["B"].player)
# print(_global.player["C"].player)
# print(_global.player["D"].player)

#play loops
nextTurn = True
stepNr = 0
while nextTurn:
	playerLetter = chr((stepNr % 4) + 65)
	pLayerObject = _global.players[playerLetter]
	playerName = pLayerObject.name
	print("Next player is {0}".format(playerName))
	print("Press <SPACE> for dice roll or <q> for Quit game!")
	while True:
		key_event = keyboard.read_event()
		if key_event.event_type == keyboard.KEY_UP and key_event.name == 'q':
			answer = input ("\bDo you really want to quit game? (y/n and enter)")
			if answer == "y":
				print("\bQuit game... Bye.")
				sys.exit()
			else:
				print("Next player is {0}".format(_global.players[playerLetter].name))
		elif key_event.event_type == keyboard.KEY_UP and key_event.name == 'space':
			key_event = None
			break
	diceRoll = random.randint(1,6)
	print(diceRoll)

	#at the end of a step:
	stepNr += 1






sys.exit()


# player1 = Player("A")
#


print(players["A"].playerPrintout())
print(players["B"].playerPrintout())
print(players["C"].playerPrintout())

# table szakasz
# table1.tablePrintout()
# table1.fullPrintout()





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

# test if someone has won
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
