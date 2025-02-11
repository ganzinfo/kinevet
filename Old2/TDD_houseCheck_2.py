
def houseCheck(fieldBefore, diceRoll, testHouseFields):
    #   H 1,2,3,4
    #   0 ha nem ért be
    targetField = -1  # only for testing
    maxTarget = fieldBefore + diceRoll
    lastPossible = -1
    condition = True
    checkedField = 41
    while (condition):
        if checkedField > maxTarget:
            condition = False
            break
        if testHouseFields[checkedField - 41] == 0:
            lastPossible = checkedField - 40
        if checkedField == 44:
            condition = False
        checkedField += 1
    # if testHouseFields[calculatedTarget-41] == 0:
    #     targetField = calculatedTarget-40
    return lastPossible

