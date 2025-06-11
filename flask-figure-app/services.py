from models import Square, Circle, Triangle

class FigureService:
    def __init__(self):
        self.figures = {
            "square": Square(),
            "circle": Circle(),
            "triangle": Triangle()
        }

    def get_all_colors(self):
        return {name: fig.get_color() for name, fig in self.figures.items()}

    def set_color(self, figure_type, color):
        if figure_type in self.figures:
            self.figures[figure_type].set_color(color)
            return True
        return False

    def set_color_all(self, color):
        for fig in self.figures.values():
            fig.set_color(color)
