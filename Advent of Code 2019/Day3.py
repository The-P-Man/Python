path = ['R8', 'U5', 'L5', 'D3']


def get_coords(path):
    coords = [(0, 0)]
    for cmd in path:
        r, n = cmd[0], cmd[1]
        if r == 'R':
            x, y = 1, 0
        elif r == 'L':
            x, y = -1, 0
        elif r == 'U':
            x, y = 0, 1
        else:
            x, y = 0, -1
        for i in range(1, int(n)+1):
            coords.append((coords[-1][0] + x, coords[-1][1] + y))
    return coords

coords1 = get_coords(path)
print(coords1)

