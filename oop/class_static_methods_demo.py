# oop/class_static_methods_demo.py

class Calculator:
    """A simple Calculator class demonstrating static and class methods."""

    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """Static method to return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """Class method to return the product of two numbers.
        Prints the calculation type before performing the operation.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
