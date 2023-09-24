from plum import dispatch
from src.shapes import Square, Circle
from math import pi
from typing import overload
from numba import njit


@dispatch
def area(s: Square) -> float:
    """Calculates the area of a square"""
    return s.side**2


@dispatch
def area(c: Circle) -> float:
    """Calculates the radius of a circle"""
    return pi * c.radius**2


if __name__ == "__main__":
    s = Square(side=4.0)
    c = Circle(radius=2.5)

    print(area(s))
    print(area(c))
