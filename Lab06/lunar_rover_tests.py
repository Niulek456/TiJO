import unittest
from lunar_rover import LunarRover

class LunarRoverTestCase(unittest.TestCase):
    def setUp(self):
        self.rover = LunarRover()

    def test_initial_position(self):
        self.assertEqual(self.rover.get_position(), (0, 0, 'N'))

    def test_move_forward(self):
        self.rover.move_forward()
        self.assertEqual(self.rover.get_position(), (0, 1, 'N'))

    def test_move_backward(self):
        self.rover.move_backward()
        self.assertEqual(self.rover.get_position(), (0, -1, 'N'))

    def test_rotate_left(self):
        self.rover.rotate_left()
        self.assertEqual(self.rover.get_position(), (0, 0, 'W'))

    def test_rotate_right(self):
        self.rover.rotate_right()
        self.assertEqual(self.rover.get_position(), (0, 0, 'E'))

    def test_complex_movement(self):
        self.rover.move_forward()
        self.rover.rotate_right()
        self.rover.move_forward()
        self.assertEqual(self.rover.get_position(), (1, 1, 'E'))

if __name__ == "__main__":
    unittest.main()
