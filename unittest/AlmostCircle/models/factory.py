"""Factory methods return a new instance/object
for several use cases."""

class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"Square of side length {self.side} units."


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    @classmethod
    def frm_square(cls, square):
        # returns an instance
        return cls(length=square.side, breadth=square.side)

    def __str__(self):
        return f"Rectangle with dimensions {self.length}x{self.breadth}."


def main():
    square_box = Square(10)
    rectangle_box = Rectangle.frm_square(
        square_box
    )  # calling class method from class.
    print(rectangle_box)


if __name__ == "__main__":
    main()
