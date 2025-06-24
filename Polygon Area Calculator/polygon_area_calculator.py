class Rectangle:
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.

        Parameters:
            width (int or float): The width of the rectangle.
            height (int or float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def set_width(self, width):
        """
        Sets the width of the rectangle.

        Parameters:
            width (int or float): The width of the rectangle.
        """
        self.width = width

    def set_height(self, height):
        """
        Sets the height of the rectangle.

        Parameters:
            height (int or float): The height of the rectangle.
        """
        self.height = height
    
    def get_area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int or float: The area of the rectangle.
        """
        return (self.width * self.height)

    def get_perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int or float: The perimeter of the rectangle.
        """
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        """
        Calculates and returns the diagonal of the rectangle using the Pythagorean theorem.

        Returns:
            float: The length of the diagonal of the rectangle.
        """
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        """
        Generates a string representation of the rectangle as asterisks (*),
        with the height and width of the rectangle defining the number of
        rows and columns, respectively.

        If the rectangle is too large (height > 50, width > 50), returns
        'Too big for picture.'

        Returns:
            str: A string representation of the rectangle as asterisks.
        """
        if self.height > 50 or self.width > 50:
            return f'Too big for picture.'
        picture = []
        for i in range(self.height):
            ast = "*" * self.width
            picture.append(f'{ast}\n')
        return ''.join(picture)

    def get_amount_inside(self, other):
        """
        Calculates and returns the amount of other rectangles that can fit inside
        the current rectangle.

        Parameters:
            other (Rectangle or Square): The rectangle or square to calculate the
                amount of fitting inside the current rectangle.

        Returns:
            int: The amount of other rectangles that can fit inside the current
                rectangle.
        """
        area1 = self.get_area()
        area2 = other.get_area()

        return (area1 // area2)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        The string includes the width and height of the rectangle
        formatted as 'Rectangle(width={width}, height={height})'.

        Returns:
            str: A string representation of the rectangle.
        """
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side):
        """
        Initializes a Square instance with side.

        Parameters:
            side (int or float): The length of the side of the square.
        """
        super().__init__(side, side)

    def set_side(self, side):
        """
        Sets the side of the Square instance.

        Parameters:
            side (int or float): The length of the side of the square.
        """
        super().set_width(side)
        super().set_height(side)

    def set_width(self, width):
        """
        Sets the width of the square.

        Since the square has equal length sides, setting the width
        automatically sets the height as well.

        Parameters:
            width (int or float): The width of the square.
        """
        self.set_side(width)

    def set_height(self, height):
        """
        Sets the height of the square.

        Since the square has equal length sides, setting the height
        automatically sets the width as well.

        Parameters:
            height (int or float): The height of the square.
        """
        self.set_side(height)

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        The string representation includes the length of the side of the square.

        Returns:
            str: A string representation of the Square instance.
        """
        return f'Square(side={self.width})'


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))