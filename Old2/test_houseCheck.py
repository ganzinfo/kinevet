import pytest
import TDD_houseCheck_2
@pytest.mark.parametrize("actPos,diceRoll,houseState,expected ",
[
(39,1,(0,2,0,3),-1),
(39,2,(0,2,0,3),1),
(39,3,(0,2,0,3),1),
(39,4,(0,2,0,3),3),
(39,5,(0,2,0,3),3),
(39,6,(0,2,0,0),4)
])
def test_houseCheck(actPos, diceRoll, houseState,expected):

    assert(TDD_houseCheck_2.houseCheck(actPos, diceRoll, houseState) == expected)