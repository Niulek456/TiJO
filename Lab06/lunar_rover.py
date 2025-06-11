class LunarRover:
    def __init__(self, x=0, y=0, direction='N'):
        self.x = x
        self.y = y
        self.direction = direction
        self.directions = ['N', 'E', 'S', 'W']

    def move_forward(self):
        match self.direction:
            case 'N': self.y += 1
            case 'S': self.y -= 1
            case 'E': self.x += 1
            case 'W': self.x -= 1

    def move_backward(self):
        match self.direction:
            case 'N': self.y -= 1
            case 'S': self.y += 1
            case 'E': self.x -= 1
            case 'W': self.x += 1

    def rotate_left(self):
        idx = (self.directions.index(self.direction) - 1) % 4
        self.direction = self.directions[idx]

    def rotate_right(self):
        idx = (self.directions.index(self.direction) + 1) % 4
        self.direction = self.directions[idx]

    def get_position(self):
        return (self.x, self.y, self.direction)
