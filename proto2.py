"""
A játékos saját koordinátarendszere és a tábla koordinátarendszere közötti átváltás megvalósítása

"""
def ucoordToTable(userPos, offset): #User coordinate convert to table coordinate
    return (userPos+offset) % 40

def tcoordToUser(tablePos, offset): #Table coordinate convert to user coordinate
    return (tablePos+40-offset) % 40

uCoord = {}
tCoord = {}
offset = 10

for i in range(40):
    uCoord[i+1] = []
    tCoord[i+1] = []

print(uCoord,"\n", tCoord)

print(ucoordToTable(36,offset))
print(tcoordToUser(6,offset))

