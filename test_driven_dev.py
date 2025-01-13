import TDD_houseCheck
#import pytest

testdata = ()
testdata.append (39,1,(0,2,0,3),-1)
testdata.append (39,2,(0,2,0,3),1)
testdata.append (39,3,(0,2,0,3),1)
testdata.append (39,4,(0,2,0,3),3)
testdata.append (39,5,(0,2,0,3),3)
testdata.append (39,6,(0,2,0,0),4)

#Házi feladat: kétszintű tuple-ba tenni a tesztadatokat.

#@pytest.mark.xfail
def test_houseCheck():
    for data in testdata:
        startfield = data[0]
        diceRoll = data[1]
        testHouseFields=data[2]
        expectedValue = data[3]
        #assert TDD_houseCheck.houseCheck(startfield, diceRoll, testHouseFields) == expectedValue
        print(data)


print(testdata)
#test_houseCheck()