# 1-40 - H1-H4
# 11-10 -
# 21-20
# 31-30

loop = {}

def loopPrint():
    printout = ""
    for i in range(40):
        printout += "("
        printout += str(i+1)
        printout += ":"
        printout += str(loop[i+1][0])
        printout += str(loop[i+1][1])
        printout += ")"
        if (i+1) % 5 == 0:
            printout += "\n"

    print(printout)

def playerLoop(player):
    """A játékosok saját köre a tábla koordinátarendszerében, házzal együtt.
    Ezen csak végig kell mennie.
    A házban a szabály alapján speciális a viselkedés.
    """
    for i in range (40):
        start = startFields[player]
        print (i,"  ",(40 + start-1 + i ) % 40+1)
    for j in range(4):
        j += 1
        print (j,"  ",(40 + start-1 + i ) % 40+1+j)

"""
A házba érés problematikája. Könnyű verzó: Ha többet dob, de beér a házba, az utolsó szabad helyig mehet, ahova elér, de a házban marad. Ez a verzó marad.
Ezt matematikailag is le kellene írni.
A nehezebb verzió: A házban a két végén visszafordulva addig kell lépegetnie, amíg ... Ez az utolsó szabad helynél már úgysem működik. El lehet vetni.
"""

def houseFilling():



for i in range(40):
    loop[i+1] = ("_",0,0)

# loopPrint()

startFields = {}

startFields['A']=1
startFields['B']=11
startFields['C']=21
startFields['D']=31

for i in range(4):
    playerLoop(chr(65+i))