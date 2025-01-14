# import assume
import TDD_houseCheck
import pytest

#Házi feladat: kétszintű tuple-ba tenni a tesztadatokat.

#@pytest.mark.xfail
@pytest.mark.parametrize("startfield,diceRoll,testHouse,expected ",
[
(39,1,(0,2,0,3),0),
(39,2,(0,2,0,3),1),
(39,3,(0,2,0,3),1),
(39,4,(0,2,0,3),3),
(39,5,(0,2,0,3),3),
(39,6,(0,2,0,0),4)
])
def test_houseCheck(startfield, diceRoll, testHouse, expected):
    assert(TDD_houseCheck.houseCheck(startfield, diceRoll, testHouse) == expected)
