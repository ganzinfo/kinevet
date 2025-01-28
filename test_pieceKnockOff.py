import pytest
from table import Table


@pytest.mark.parametrize("param1", [1, 2])
def test_pieceKnockOff(param1):
    #creating the game state:
    table = Table()
    table["S"]["A"]= 3
    table.tablePrintout()
    # table.fullPrintout()
    assert (param1 == 1)
