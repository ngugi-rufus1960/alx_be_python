# oop/polymorphism_demo.py

import math


class Shape:
    """Base class representing a generic shape."""

    def area(self):
        """Abstract method to compute the area of a shape.
        Must be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    """Derived class representing a rectangle."""

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Return the area of the rectangle (length × width)."""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Return the area of the circle (π × r²)."""
        return math.pi * (self.radius ** 2)
