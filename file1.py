import pytest


@pytest.mark.usefixtures("fixture1","fixture2")
class TestAnyclassname:
    def test_method1(self):
        print("test_method1")

    def test_method2(self):
        print("test_method2")


