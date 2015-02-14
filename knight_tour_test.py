#!/usr/bin/python
import unittest
from random import randint
from knight import DESK_X_SIZE, DESK_Y_SIZE, get_the_route


def is_move_correct(x1, y1, x2, y2):
    """
    Checks if a given Horse move from (x1, y1) to (x2, y2)
    is correct Horse move.
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """
    # Check that there is not negative coordinates
    if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
        return False

    # Check there is not coordinates out of desk
    if x1 >= DESK_X_SIZE or x2 >= DESK_X_SIZE or y1 >= DESK_Y_SIZE or y2 >= DESK_Y_SIZE:
        return False

    # Check that X delta is 2 and Y delta is 1. Or vice versa.
    if (abs(x1-x2) == 2 and abs(y1-y2) == 1) or (abs(x1-x2) == 1 and abs(y1-y2) == 2):
        return True

    return False


class TestKnightsTourIsValid(unittest.TestCase):
    def setUp(self):
        self.route = get_the_route(randint(0, 7), randint(0, 7))

    def test_knight_tour(self):
        """
        Need validate 2 things here:
         - First - validate that every following move is correct Knight move.
         - Second - that total number of moves is equal to number of cells on the desk
         and each cell appears only once. This means that every cell is visited, and visited
         only once.
        :return:
        """

        # Let's validate that all cells are visited
        self.assertTrue(len(self.route) == DESK_X_SIZE*DESK_Y_SIZE)
        self.assertTrue(len(self.route) == len(set(self.route)))

        # Now let's validate that all moves are correct Knight moves
        prev = self.route[0]

        for following in self.route[1:]:
            x1, y1 = prev
            x2, y2 = following
            self.assertTrue(is_move_correct(x1, y1, x2, y2))
            prev = following

if __name__ == "__main__":
    unittest.main()