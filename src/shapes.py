from dataclasses import dataclass
from abc import ABCMeta


class AbstractShape(metaclass=ABCMeta):
    """ Abstract class for a shape"""
    pass


@dataclass
class Square(AbstractShape):
    """ Square shape class"""
    side: float


@dataclass
class Circle(AbstractShape):
    """ A circle geometric shape"""
    radius: float
