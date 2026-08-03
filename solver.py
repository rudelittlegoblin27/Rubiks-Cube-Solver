def solved_cube():
    """Returns a fresh, solved cube. Each face is a list of 9 stickers."""
    return {
        'U': ['W'] * 9,  # Up = White
        'D': ['Y'] * 9,  # Down = Yellow
        'F': ['G'] * 9,  # Front = Green
        'B': ['B'] * 9,  # Back = Blue
        'L': ['O'] * 9,  # Left = Orange
        'R': ['R'] * 9,  # Right = Red
    }


def print_cube(cube):
    """Prints the cube as an unfolded cross so you can see it."""
    def row(face, start):
        return ' '.join(cube[face][start:start + 3])

    for i in range(0, 9, 3):
        print('      ' + row('U', i))
    print()
    for i in range(0, 9, 3):
        print(row('L', i), row('F', i), row('R', i), row('B', i))
    print()
    for i in range(0, 9, 3):
        print('      ' + row('D', i))


if __name__ == '__main__':
    cube = solved_cube()
    print_cube(cube)