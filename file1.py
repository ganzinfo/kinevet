import pytest


@pytest.mark.usefixtures("fixture1","fixture2")
class Testclass:

    def test_method1(fixture1):
        print("test_method1")

    def test_method2(fixture1):
        print("test_method2")


