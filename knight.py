#!/usr/bin/python
"""
Implementation of the Knight's tour problem solution
(https://en.wikipedia.org/wiki/Knight%27s_tour)
using Warnsdorff's heuristic rule, which works well for 8*8 desk
(it also works well for from 5*5 to 76*76 desks), and resolves the
problem in linear time.
"""
import sys

DESK_X_SIZE = 8
DESK_Y_SIZE = 8


def get_available_moves(x, y, desk):
    """
    Return a list of available Horse moves from x, y coordinate o the 'desk'.
    In common case we have 8 available moves: x+-2, x+-1, y+-2,y+-1, dx+dy=3.
    :param x:
    :param y:
    :param desk:
    :return:
    """
    # all variants of dx, dy pairs
    available_deltas = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    result = []

    for move in [(x+dx, y+dy) for dx, dy in available_deltas]:
        # check if we trespass the desk borders
        if (0 <= move[0] < DESK_X_SIZE) and (0 <= move[1] < DESK_Y_SIZE):
            # if those cell is not already visited
            if not desk[move[0]][move[1]]:
                result.append(move)

    return result


def get_the_route(x, y):
    """
    Suppose we have 8*8 chess desk.
    :param x:
    :param y:
    :return: a list of tuples (x,y) - a sequence of Horse's steps
    that should satisfy problem conditions. X, Y a both numbers starting from 0.

    """
    # Assume that first desk index mean X coordinate, second one - Y.
    # X_SIZE*Y_SIZE matrix filled with zeros
    desk = []
    for i in range(DESK_X_SIZE):
        desk.append([0]*DESK_Y_SIZE)

    # current Horse position
    current = (x, y)

    # mark start position as visited
    desk[x][y] = 1

    result = [current]

    # We want to make next move to the cell with least number of available moves
    # (Warnsdorff's rule).
    # This allows us to resolve the problem in a linear time on fields from 5*5 to 76*76
    # Our case (8*8 standard chess field) fits this restriction
    while True:
        moves_rating = {}
        available_moves = get_available_moves(current[0], current[1], desk)
        # If no more moves are available - solution is found (or deadlock is found:)
        if not available_moves:
            break

        for move in available_moves:
            moves_rating[move] = len(get_available_moves(move[0], move[1], desk))

        # Select minimum of sequence ((x, y), rating) by rating.
        move = min(moves_rating.items(), key=lambda record: record[1])[0]

        # Now we have coordinates of next move. Lets move our Horse to a given point.
        current = move
        result.append(move)

        # ...And mark appropriate desk cell as visited
        desk[move[0]][move[1]] = 1

    return result

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: ./horse.py <start_cell>, for example: ./horse.py e5 \n\n')
        sys.exit()

    if len(sys.argv) > 2:
        sys.stderr.write('Usage: ./horse.py <start_cell>, for example: ./horse.py e5. \n'
                         'Other arguments are ignored \n\n')
    cell = sys.argv[1].upper()
    if len(cell) != 2 or (cell[0] not in 'ABCDEFGH') or (cell[1] not in '12345678'):
        sys.stderr.write('Usage: ./horse.py <start_cell>, for example: ./horse.py e5\n'
                         'Program accepts only cells from standard chess board:\n'
                         'from A1 to H8. \n\n')
        sys.exit()

    # convert from coordinates from chess notation to Decart notation
    x = ord(cell[0]) - ord('A')
    y = int(cell[1]) - 1

    route = get_the_route(x, y)
    string_result = ''
    for n, move in enumerate(route):
        if n % 20 == 0:
            string_result += '\n'

        string_result += chr(move[0] + ord('A')) + str(move[1] + 1) + '  '

    sys.stdout.write('The following route found:\n')
    sys.stdout.write(string_result)
    sys.stdout.write('\n\n')