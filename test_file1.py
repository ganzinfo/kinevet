import pytest

@pytest.fixture()
def fixture1():
    print("teszt előtt...fixture1")
    yield
    print("teszt után...fixture1")

def test_method1(fixture1):
    print("Test_method1 lefutott...")


def test_method2(fixture1):
    print("Test_method2 lefutott...")

