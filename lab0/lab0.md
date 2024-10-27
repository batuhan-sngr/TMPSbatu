# **SOLID**

### **Course: Software Design Techniques and Mechanisms**
### **Author: Emre Batuhan Sungur**

----

## **Theory**
The SOLID principles are a set of five design principles aimed at making object-oriented software more understandable, flexible, and maintainable. Introduced by Robert C. Martin, these principles help developers build systems that are easy to extend, reuse, and test. 

##  Objectives:

Implement 2 SOLID letters in a simple project.


## **Implementation description**

Let’s implement two principles from SOLID in a simple project. We will use:

S - Single Responsibility Principle (SRP): Each class should have only one reason to change, meaning that a class should have only one job.
O - Open/Closed Principle (OCP): Classes should be open for extension but closed for modification, meaning you can add new functionality without changing existing code.

### **Apply the Single Responsibility Principle (SRP)**
Each shape will be responsible for calculating its own area. A `Shape` class will not manage drawing or calculating areas for multiple shapes—it will delegate that responsibility to specific classes.

- Each shape class (`Rectangle`, `Circle`, `Triangle`) has one responsibility: to calculate its area.
- The `ShapeManager` class has a single responsibility: to print the area of a shape. It does not calculate the area, thus separating concerns.

### **Apply the Open/Closed Principle (OCP)**
We will design the system in such a way that new shapes can be added without changing the existing classes. We’ll achieve this by using an abstract base class (`Shape`) and then creating concrete implementations for each shape.

- The `Shape` base class allows us to extend the system with new shapes (e.g., `Triangle`, `Hexagon`) without modifying existing shape classes.
- If a new shape is added, it will implement the `Shape` interface, and no existing code needs to be modified.

```python
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

```

## **Conclusions**
In this project, I've implemented two of the SOLID principles—Single Responsibility and Open/Closed—in a simple Shape Drawing system. Each shape class (e.g., `Rectangle`, `Circle`, `Triangle`) has a single responsibility: calculating its area. This ensures adherence to the Single Responsibility Principle (SRP), making the code easier to understand and maintain.

I've also applied the Open/Closed Principle (OCP) by designing a base class (`Shape`) that allows for easy extension. New shapes can be added to the system without modifying existing code, making the system flexible and future-proof.

These principles help in building scalable, maintainable systems by dividing responsibilities clearly and allowing for easy expansion without modifying core functionality. Through this project, we can see how the thoughtful application of SOLID principles leads to cleaner, more modular, and robust software systems.

### **References**
* https://www.geeksforgeeks.org/solid-principle-in-programming-understand-with-real-life-examples/