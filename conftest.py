import pytest
from table import Table
# import _global


def tablesetup_PieceKnockOff():
    table = Table()

    tupledata = ("A1",0)
    table.table["F"][4] = tupledata
    tupledata = ("B2",0)
    table.table["F"][7] = tupledata
    print(table.tablePrintout())

    #table.tablePrintout()
    #table.fullPrintout()


tablesetup_PieceKnockOff()