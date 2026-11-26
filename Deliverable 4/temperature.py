import math


class Temperature:
    # 1. Initialization and validation
    # Save the value and check that the temperature is valid.
    def __init__(self, value, unit='C'):
        self._unit = unit.upper()
        self._value = float(value)
        # The lowest allowed value in each unit.
        limits = {'C': -273.15, 'F': -459.67, 'K': 0}
        if self._unit not in limits:
            raise ValueError('Invalid temperature unit')
        if not math.isfinite(self._value) or self._value < limits[self._unit]:
            raise ValueError('Invalid temperature value')

    # 2. Floating-point tolerance
    TOL = 1e-9

    # 3. Read-only attributes
    # Let us read the value without changing it.
    @property
    def value(self):
        return self._value

    # Let us read the unit without changing it.
    @property
    def unit(self):
        return self._unit

    # 4. Conversion methods
    # Convert the temperature to Celsius.
    def to_celsius(self):
        if self.unit == 'K':
            return self.value - 273.15
        if self.unit == 'F':
            return (self.value - 32) * 5 / 9
        return self.value

    # Convert the temperature to Fahrenheit.
    def to_fahrenheit(self):
        if self.unit == 'F':
            return self.value
        return self.to_celsius() * 9 / 5 + 32

    # Convert the temperature to Kelvin.
    def to_kelvin(self):
        if self.unit == 'K':
            return self.value
        return self.to_celsius() + 273.15

    # Create a new temperature in the requested unit.
    def convert_to(self, target_unit):
        target_unit = target_unit.upper()
        if target_unit == 'C':
            return Temperature(self.to_celsius(), 'C')
        if target_unit == 'F':
            return Temperature(self.to_fahrenheit(), 'F')
        if target_unit == 'K':
            return Temperature(self.to_kelvin(), 'K')
        raise ValueError('Invalid temperature unit')

    # 5. String representations
    # Show how the object was created.
    def __repr__(self):
        return f'Temperature({self.value!r}, {self.unit!r})'

    # Return a simple text for print().
    def __str__(self):
        symbol = self.unit
        if self.unit != 'K':
            symbol = '°' + self.unit
        return f'{self.value:.2f} {symbol}'

    # 6. Comparisons (all temperatures in Kelvin)
    # Check if both objects have the same value.
    def __eq__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        # Compare both values in Kelvin.
        difference = abs(self.to_kelvin() - other.to_kelvin())
        return difference <= self.TOL

    # Check if the values are different.
    def __ne__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return not self == other

    # Check if the first value is smaller.
    def __lt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self.to_kelvin() < other.to_kelvin() and self != other

    # Check if the first value is smaller or equal.
    def __le__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self < other or self == other

    # Check if the first value is larger.
    def __gt__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return other < self

    # Check if the first value is larger or equal.
    def __ge__(self, other):
        if not isinstance(other, Temperature):
            return NotImplemented
        return self > other or self == other
