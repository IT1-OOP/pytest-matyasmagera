import pytest
from src import calculator

def test_devide():
    with pytest.raises(ValueError) as exc:
        calculator.divide(5, 0)
    assert str(exc.value) == "Cannot divide by zero!"

def test_devide2():
    with pytest.raises(NameError):
        calculator.divide(5,0)
