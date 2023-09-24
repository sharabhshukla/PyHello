from dataclasses import dataclass
from math import pi


@dataclass
class Square:
    """A square class"""

    side: float

    def area(self) -> float:
        """This method returns an area of the shape"""
        return self.side**2


@dataclass
class Circle:
    """A circle class"""

    radius: float

    def area(self) -> float:
        """This method returns the area of the shape"""
        return pi * self.radius**2
