# import assume
import TDD_houseCheck
import pytest

#Házi feladat: kétszintű tuple-ba tenni a tesztadatokat.
"""
A megoldás nem az egymásba ágyazott tuple vagy más adatszerkezet lett. A pytestnek saját szintaxisa van a test többszöri. paraméterezett futtatásához. Kivitelezése alább látható:
@pytest.mark.parametrize([ide jönnek a paraméterek és az értékek hozzá])
Lásd még pytest doksi.
A fejlesztéskor végiggondolt tesztadatokat így beadva 100% PASSED.
Aki nem hiszi, húzza le a gitről a repo-t és futassa ezt a fájlt.
"""

#@pytest.mark.xfail
@pytest.mark.parametrize("startfield,diceRoll,testHouse,expected ",
[
(39,1,(0,2,0,3),-1), # -1 azt jelenti, hogy az aktuális dobással be sem érünk a házba. 39+1 = 40, < 41
(39,2,(0,2,0,3),1),
(39,3,(0,2,0,3),1),
(39,4,(0,2,0,3),3),
(39,5,(0,2,0,3),3),
(39,6,(0,2,0,0),4)
])
def test_houseCheck(startfield, diceRoll, testHouse, expected):
    assert(TDD_houseCheck.houseCheck(startfield, diceRoll, testHouse) == expected)
