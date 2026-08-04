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

def rotate_face_cw(face):
    """Rotates a single face's 9 stickers 90 degrees clockwise."""
    a, b, c, d, e, f, g, h, i = face
    return [g, d, a, h, e, b, i, f, c]


def move_U(cube):
    """Applies a clockwise turn of the Up face."""
    cube['U'] = rotate_face_cw(cube['U'])

    # Save F's top row before overwriting anything
    f_top = cube['F'][0:3]

    # Shift top rows around: L -> F -> R -> B -> L
    cube['F'][0:3] = cube['R'][0:3]
    cube['R'][0:3] = cube['B'][0:3]
    cube['B'][0:3] = cube['L'][0:3]
    cube['L'][0:3] = f_top

    return cube

if __name__ == '__main__':
    cube = solved_cube()
    print_cube(cube)