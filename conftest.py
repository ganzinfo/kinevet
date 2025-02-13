import pytest


@pytest.fixture(scope = "class")
def fixture1():
    print("Előtte lefut...fixture1")
    yield
    print("utána lefut....fixture1")

@pytest.fixture
def fixture2():
    print("Előtte lefut...fixture2")
    yield
    print("utána lefut....fixture2")