import pytest
from temperature import Temperature


# 1. Initialization
# Check the default unit, lowercase units and read-only values.
def test_initialization():
    t = Temperature(25)
    assert t.value == 25
    assert t.unit == 'C'
    assert Temperature(32, 'f').unit == 'F'
    assert Temperature(0, 'k').unit == 'K'
    with pytest.raises(AttributeError):
        t.value = 10
    with pytest.raises(AttributeError):
        t.unit = 'F'


# 2. Validation
# Check that invalid temperatures give an error.
def test_validation():
    for value, unit in [(0, 'X'), (-274, 'C'), (-460, 'F'), (-1, 'K')]:
        with pytest.raises(ValueError):
            Temperature(value, unit)


# Check that an unknown target unit gives an error.
def test_invalid_conversion():
    with pytest.raises(ValueError):
        Temperature(25).convert_to('X')


# 3. Conversions
# Check all three units at the five reference temperatures.
def test_conversions():
    # Each row contains Celsius, Fahrenheit and Kelvin.
    points = [(-273.15, -459.67, 0), (-40, -40, 233.15),
              (0, 32, 273.15), (37, 98.6, 310.15), (100, 212, 373.15)]
    for c, f, k in points:
        for value, unit in [(c, 'C'), (f, 'F'), (k, 'K')]:
            t = Temperature(value, unit)
            assert abs(t.to_celsius() - c) <= 1e-9
            assert abs(t.to_fahrenheit() - f) <= 1e-9
            assert abs(t.to_kelvin() - k) <= 1e-9


# 4. Round-trip conversions
# Convert between all units and check the original value.
def test_round_trip():
    t = Temperature(25)
    result = t.convert_to('f').convert_to('K').convert_to('C')
    assert result == t
    assert result is not t


# 5. Cross-unit comparisons
# Check all comparison operators and unsupported types.
def test_comparisons():
    a = Temperature(0, 'C')
    b = Temperature(32, 'F')
    c = Temperature(300, 'K')
    assert a == b
    assert a != c
    assert a < c
    assert a <= b
    assert c > b
    assert c >= a
    assert a >= b
    assert a == Temperature(5e-10, 'C')
    assert not a < Temperature(5e-10, 'C')
    assert a.__eq__(10) is NotImplemented
    assert a.__ne__(10) is NotImplemented
    assert a.__lt__(10) is NotImplemented
    assert a.__le__(10) is NotImplemented
    assert a.__gt__(10) is NotImplemented
    assert a.__ge__(10) is NotImplemented


# 6. Formatting
# Check the text returned by str() and repr().
def test_formatting():
    t = Temperature(25)
    assert str(t) == '25.00 °C'
    assert repr(t) == "Temperature(25.0, 'C')"
