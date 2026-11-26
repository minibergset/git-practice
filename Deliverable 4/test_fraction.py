import pytest
from fraction import Fraction


# 1. Initialization
# Check valid fractions and invalid inputs.
def test_initialization():
    f = Fraction(1, 2)
    assert f.numerator == 1
    assert f.denominator == 2
    for denominator in [0, -2]:
        with pytest.raises(ValueError):
            Fraction(1, denominator)
    with pytest.raises(TypeError):
        Fraction(1.5, 2)
    with pytest.raises(TypeError):
        Fraction(1, 2.5)


# 2. Comparisons
# Check all six comparison operators.
def test_comparisons():
    a = Fraction(1, 2)
    b = Fraction(2, 4)
    c = Fraction(3, 4)
    assert a == b
    assert a != c
    assert a < c
    assert a <= b
    assert c > a
    assert c >= b
    assert a >= b
    assert Fraction(-1, 2) < a


# 3. Four other special methods
# Check the simple fraction text.
def test_str():
    assert str(Fraction(1, 2)) == '1/2'


# Check the object representation.
def test_repr():
    assert repr(Fraction(1, 2)) == 'Fraction(1, 2)'


# Check that addition gives the correct fraction.
def test_add():
    assert Fraction(1, 2) + Fraction(1, 4) == Fraction(3, 4)


# Check that multiplication gives the correct fraction.
def test_mul():
    assert Fraction(1, 2) * Fraction(2, 3) == Fraction(1, 3)
