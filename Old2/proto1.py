class Game:

    def __init__(self) -> None:
        print('__init__')
        # self.main()
        self.playerCount = 0
        self.players = {}
        """player dict (key:Betűjele, value:neve )"""

        valasztas = self.fomenu()
        print("valasztas: ", valasztas, type(valasztas))
        if valasztas == "1":
            self.playernames()

    # print('vege')

    def fomenu(self):
        print('fomenu')
        print(
            "Udvozollek a jatekban!",
            "\nFomenu:\n\tUj jatek \t\t(1)\n\tJatek betoltese (2)\n\tKilepes \t\t(3)\n Valasztas:"
        )
        answer = input()
        return answer

    def main(self) -> None:
        print('main')
        while True:
            answer = self.fomenu()
            """
            match (answer):
                case '1':
                    print('uj jatek')
                    break
                case '2':
                    print('Jatek betoltese')
                    break
                case '3':
                    print('Kilepes')
                    exit()
                case _:
                    print('Valassz ujra!')
                """

    # print('while utan')

    def playernames(self):
        print("playernames")
        count = 1
        maxcount = int(input("Hany jatekos legyen?"))
        while True:
            """Bekérjük a játéskosok neveit"""
            print("Kérem az " + str(count) + ". jatekos nevét:")
            name = input()
            self.players[chr(count + 64)] = name
            if count == maxcount:
                break
            if count > 4:
                print("Maximum négyen játszhatnak")
                break
            count += 1
        print(self.players)


"""
#creating the table in a dictionary
#keys: numbers, values: list with two strings


def create_table():
		table = {}
		for i in range(40):
		#["fied type","field content"]  
			table[i] = ["", ""]
		#set special fields

		return table
"""
