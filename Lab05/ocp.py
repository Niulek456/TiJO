class Figure:
    def draw(self):
        raise NotImplementedError

class Square(Figure):
    def __init__(self, a):
        self.a = a

    def draw(self):
        for _ in range(self.a):
            print(self.a * "o")
        print()

class Triangle(Figure):
    def __init__(self, h):
        self.h = h

    def draw(self):
        for i in range(1, self.h + 1):
            print(i * "o")
        print()

class FigureDrawer:
    def draw(self, figure: Figure):
        figure.draw()

drawer = FigureDrawer()
drawer.draw(Square(5))
drawer.draw(Triangle(5))
