
import pytest

def test_method1(fixture1):
    print("test_method1...fixture1")

def test_method2(fixture2):
    print("test_method1...fixture1")

@pytest.fixture
def fixture1():
    print("Előtte lefut...fixture1")
    yield
    print("utána lefut....fixture1")
    
@pytest.fixture
def fixture2():
    print("Előtte lefut...fixture2")
    yield
    print("utána lefut....fixture2")