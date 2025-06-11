class RulesOfGame:
    """
    Metoda zwraca true, tylko gdy przejście z pola source na destination w jednym ruchu
    jest zgodne z zasadami gry w szachy.
    """
    def is_correct_move(self, source, destination):
        raise NotImplementedError("Subklasa musi nadpisać tę metodę.")


class Bishop(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        x1, y1 = source
        x2, y2 = destination
        return abs(x1 - x2) == abs(y1 - y2) and source != destination


class Knight(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        x1, y1 = source
        x2, y2 = destination
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        return (dx, dy) in [(2, 1), (1, 2)]


class King(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        dx = abs(source[0] - destination[0])
        dy = abs(source[1] - destination[1])
        return max(dx, dy) == 1


class Queen(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        dx = abs(source[0] - destination[0])
        dy = abs(source[1] - destination[1])
        return (dx == dy or dx == 0 or dy == 0) and source != destination


class Rook(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        x1, y1 = source
        x2, y2 = destination
        return (x1 == x2 or y1 == y2) and source != destination


class Pawn(RulesOfGame):
    def is_correct_move(self, source, destination):
        if source is None or destination is None:
            return False
        x1, y1 = source
        x2, y2 = destination
        # Zakładamy, że to pionek biały poruszający się w górę (y rośnie)
        return x1 == x2 and ((y2 - y1 == 1) or (y1 == 1 and y2 - y1 == 2))
