# solver.py

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


def rotate_face_ccw(face):
    """Rotates a single face's 9 stickers 90 degrees counter-clockwise."""
    a, b, c, d, e, f, g, h, i = face
    return [c, f, i, b, e, h, a, d, g]


def move_U(cube):
    """Applies a clockwise turn of the Up face."""
    cube['U'] = rotate_face_cw(cube['U'])

    f_top = cube['F'][0:3]

    cube['F'][0:3] = cube['R'][0:3]
    cube['R'][0:3] = cube['B'][0:3]
    cube['B'][0:3] = cube['L'][0:3]
    cube['L'][0:3] = f_top

    return cube


def move_U_prime(cube):
    """Applies a counter-clockwise turn of the Up face (undoes move_U)."""
    cube['U'] = rotate_face_ccw(cube['U'])

    f_top = cube['F'][0:3]

    cube['F'][0:3] = cube['L'][0:3]
    cube['L'][0:3] = cube['B'][0:3]
    cube['B'][0:3] = cube['R'][0:3]
    cube['R'][0:3] = f_top

    return cube


def move_D(cube):
    """Applies a clockwise turn of the Down face."""
    cube['D'] = rotate_face_cw(cube['D'])

    f_bottom = cube['F'][6:9]

    cube['F'][6:9] = cube['L'][6:9]
    cube['L'][6:9] = cube['B'][6:9]
    cube['B'][6:9] = cube['R'][6:9]
    cube['R'][6:9] = f_bottom

    return cube


def move_D_prime(cube):
    """Applies a counter-clockwise turn of the Down face (undoes move_D)."""
    cube['D'] = rotate_face_ccw(cube['D'])

    f_bottom = cube['F'][6:9]

    cube['F'][6:9] = cube['R'][6:9]
    cube['R'][6:9] = cube['B'][6:9]
    cube['B'][6:9] = cube['L'][6:9]
    cube['L'][6:9] = f_bottom

    return cube


if __name__ == '__main__':
    cube = solved_cube()
    print("Solved:")
    print_cube(cube)

    move_D(cube)
    move_D_prime(cube)

    print("\nAfter D then D' (should match the solved cube above):")
    print_cube(cube)