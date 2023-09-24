# Object-Oriented Programming (OOP) vs. Multiple Dispatch

In software development, there are various approaches to solve problems and structure code. Two common paradigms are Object-Oriented Programming (OOP) and Multiple Dispatch. Let's explore these concepts using the example of calculating the area of a circle and a square.

## Object-Oriented Programming (OOP)

OOP is a programming paradigm that organizes code around objects, which are instances of classes. Each object encapsulates data (attributes) and behaviors (methods) related to a specific concept or entity.

### Example: Calculating Area Using OOP

Let's create classes for Circle and Square, where each class has a method to calculate its area.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14159 * self.radius ** 2

class Square:
    def __init__(self, side_length):
        self.side_length = side_length
    
    def calculate_area(self):
        return self.side_length ** 2

```python
@dispatch(Circle)
def calculate_area(shape):
    return 3.14159 * shape.radius ** 2

@dispatch(Square)
def calculate_area(shape):
    return shape.side_length ** 2

