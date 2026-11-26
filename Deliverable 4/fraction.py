class Fraction:
    # 1. Initializer
    # Check the two integers and save them.
    def __init__(self, numerator, denominator):
        if type(numerator) is not int or type(denominator) is not int:
            raise TypeError('Numerator and denominator must be integers')
        if denominator <= 0:
            raise ValueError('Denominator must be positive')
        self.numerator = numerator
        self.denominator = denominator

    # 2. Comparisons using cross multiplication
    # Check if both objects have the same value.
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        # Cross multiply to compare without rounding.
        left = self.numerator * other.denominator
        right = other.numerator * self.denominator
        return left == right

    # Check if the values are different.
    def __ne__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return not self == other

    # Check if the first value is smaller.
    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        # Cross multiply to compare without rounding.
        left = self.numerator * other.denominator
        right = other.numerator * self.denominator
        return left < right

    # Check if the first value is smaller or equal.
    def __le__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self < other or self == other

    # Check if the first value is larger.
    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return other < self

    # Check if the first value is larger or equal.
    def __ge__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return self > other or self == other

    # 3. Four other special methods
    # Return a simple text for print().
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    # Show how the object was created.
    def __repr__(self):
        return f'Fraction({self.numerator}, {self.denominator})'

    # Use a common denominator to add two fractions.
    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        numerator = (self.numerator * other.denominator
                     + other.numerator * self.denominator)
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    # Multiply the numerators and the denominators.
    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)
