import pytest
from src import calculator

def test_correct_results():
    assert calculator.solve_quadratic_formula(1, -3, 2) == (2.0, 1.0)
    assert calculator.solve_quadratic_formula(1, 2, 1) == (-1.0, -1.0)
    assert calculator.solve_quadratic_formula(2, 5, -3) == (0.5, -3.0)


def test_type_error():
    with pytest.raises(TypeError):
        calculator.solve_quadratic_formula("a", 2, 3)
    with pytest.raises(TypeError):
        calculator.solve_quadratic_formula(1, "b", 3)
    with pytest.raises(TypeError):
        calculator.solve_quadratic_formula(1, 2, "c")

def test_zero_a():
    with pytest.raises(SyntaxError):
        calculator.solve_quadratic_formula(0, 2, 3)

def test_b_equals_five():
    with pytest.raises(NameError):
        calculator.solve_quadratic_formula(1, 5, 1)

def test_negative_discriminant():
    with pytest.raises(ValueError):
        calculator.solve_quadratic_formula(1, 2, 3)

