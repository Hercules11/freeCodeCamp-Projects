class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ('*' * self.width + '\n') * self.height

    def get_amount_inside(self, shape):
        if isinstance(shape, Square):
            x_axios = self.width // shape.width
            y_axios = self.height // shape.height
            return x_axios * y_axios
        else:
            x_axios = self.width // shape.width
            y_axios = self.height // shape.height
            return x_axios * y_axios
        #     x * shape.width + y * shape.height <= self.width
        #     x * shape.height + y * shape.width <= self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.height = side
        self.width = side

    def set_height(self, height):
        self.height = height
        self.width = height

    def set_width(self, width):
        self.height = width
        self.width = width

    def __str__(self):
        return f"Square(side={self.height})"
