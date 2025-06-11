class Figure:
    def __init__(self, name, color="#808080"):
        self.name = name
        self.color = color

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color


class Square(Figure):
    def __init__(self, color="#808080"):
        super().__init__("square", color)


class Circle(Figure):
    def __init__(self, color="#808080"):
        super().__init__("circle", color)


class Triangle(Figure):
    def __init__(self, color="#808080"):
        super().__init__("triangle", color)
