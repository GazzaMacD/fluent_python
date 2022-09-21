from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        * Note - if no __str__ is available
        python will call __repr__ as fallback.
        """
        return rf"Vector({self.x}, {self.y})"

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# Testing

# Test that repr method works
v1 = Vector(2, 4)
v2 = Vector(5, 6)
print(v1)

# Test two vectors added using the __add__ method with +
v3 = v1 + v2
print(f"v3 => {v3}")

# Get the magnitude of the vector using abs() implemented with __abs__
print(f"Magnitude of v3 => {abs(v3)}")
