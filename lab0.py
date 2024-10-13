from abc import ABC, abstractmethod

# Base class for all shapes - follows OCP
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

# Rectangle class with SRP (responsible only for calculating its area)
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

# Circle class with SRP (responsible only for calculating its area)
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.1416 * (self.radius ** 2)

# Triangle class with SRP (responsible only for calculating its area)
class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height

# Shape Manager class to demonstrate usage
class ShapeManager:
    @staticmethod
    def print_area(shape: Shape):
        print(f"The area is: {shape.area()}")

# Example usage
if __name__ == "__main__":
    rectangle = Rectangle(10, 5)
    circle = Circle(7)
    triangle = Triangle(6, 4)

    ShapeManager.print_area(rectangle)  # Outputs: The area is: 50
    ShapeManager.print_area(circle)     # Outputs: The area is: 153.9384
    ShapeManager.print_area(triangle)   # Outputs: The area is: 12
