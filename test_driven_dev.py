# import assume
import TDD_houseCheck
import pytest

# testdata = set()
# testdata.add((39,1,(0,2,0,3),-1))
# testdata.add ((39,2,(0,2,0,3),1))
# testdata.add ((39,3,(0,2,0,3),1))
# testdata.add ((39,4,(0,2,0,3),3))
# testdata.add ((39,5,(0,2,0,3),3))
# testdata.add ((39,6,(0,2,0,0),4))

#Házi feladat: kétszintű tuple-ba tenni a tesztadatokat.

#@pytest.mark.xfail
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_houseCheck(startfield, diceRoll, testHouse):
    for data in testdata:
        startfield = data[0]
        diceRoll = data[1]
        testHouseFields=data[2]
        expectedValue = data[3]
        pytest.assume(TDD_houseCheck.houseCheck(startfield, diceRoll, testHouseFields) == expectedValue)
        print(data)


# print(testdata)
#test_houseCheck()