# Day 10

import numpy as np
from itertools import cycle

field = '''
....#.....#.#...##..........#.......#......
.....#...####..##...#......#.........#.....
.#.#...#..........#.....#.##.......#...#..#
.#..#...........#..#..#.#.......####.....#.
##..#.................#...#..........##.##.
#..##.#...#.....##.#..#...#..#..#....#....#
##...#.............#.#..........#...#.....#
#.#..##.#.#..#.#...#.....#.#.............#.
...#..##....#........#.....................
##....###..#.#.......#...#..........#..#..#
....#.#....##...###......#......#...#......
.........#.#.....#..#........#..#..##..#...
....##...#..##...#.....##.#..#....#........
............#....######......##......#...#.
#...........##...#.#......#....#....#......
......#.....#.#....#...##.###.....#...#.#..
..#.....##..........#..........#...........
..#.#..#......#......#.....#...##.......##.
.#..#....##......#.............#...........
..##.#.....#.........#....###.........#..#.
...#....#...#.#.......#...#.#.....#........
...####........#...#....#....#........##..#
.#...........#.................#...#...#..#
#................#......#..#...........#..#
..#.#.......#...........#.#......#.........
....#............#.............#.####.#.#..
.....##....#..#...........###........#...#.
.#.....#...#.#...#..#..........#..#.#......
.#.##...#........#..#...##...#...#...#.#.#.
#.......#...#...###..#....#..#...#.........
.....#...##...#.###.#...##..........##.###.
..#.....#.##..#.....#..#.....#....#....#..#
.....#.....#..............####.#.........#.
..#..#.#..#.....#..........#..#....#....#..
#.....#.#......##.....#...#...#.......#.#..
..##.##...........#..........#.............
...#..##....#...##..##......#........#....#
.....#..........##.#.##..#....##..#........
.#...#...#......#..#.##.....#...#.....##...
...##.#....#...........####.#....#.#....#..
...#....#.#..#.........#.......#..#...##...
...##..............#......#................
........................#....##..#........#
'''

# Conver the string to a numpy array
arr = np.array([list(row) for row in field.strip().split()], dtype='U8')
field = arr.copy()
print('Before\n', arr)
m, n = arr.shape


def get_props(origin, target):
    '''Returns the bearing between two coordinates'''
    x = target[1] - origin[1]
    y = -target[0] + origin[0]
    theta = np.arctan2(x, y) * 180 / np.pi
    r = round(np.sqrt(x**2 + y**2), 2)
    if x < 0:
        theta = 360 + theta
    return r, int(100*theta)


def get_asteroids(origin):
    '''Updates an asteroid with number of visible asteroids'''
    coords = []
    angles = []
    distances = []
    for i in range(m):
        for j in range(n):
            target = (i, j)
            if origin != target and field[target] != '.':
                r, theta = get_props(origin, target)
                coords.append(target)
                angles.append(theta)
                distances.append(r)
    number = len(set(angles))
    arr[origin] = str(number)
    return coords, angles, distances


for i in range(m):
    for j in range(n):
        origin = (i, j)
        if arr[origin] == '#':
            get_asteroids(origin)


# Convert the strings to integers and print answer
arr[arr=='.'] = '0'
arr = arr.astype(int)
print('After\n', arr)

pov = (arr.argmax() // m, arr.argmax() % n)
print(f'{arr.max()} asteroids detected at {pov}')
field[pov] = 'X'


# # Write the field map to a text file
# with open('field.txt', 'w') as f:
#     for line in field:
#         f.writelines(line)
#         f.writelines('\n')


coords, angles, distances = get_asteroids(pov)

# coords = np.array(coords)
angles = np.array(angles)
distances = np.array(distances)
order = np.lexsort((distances, angles))
angles = angles[order]

unique_angles = sorted(list(set(angles)))

for i, angle in enumerate(unique_angles):
    ind = order[angles == angle][0]
    coord = coords[ind]
    field[coord] = 'o'
    if 100 <= i and i < 110:
        field[coord] = str(i-100)
    # if i == 199:
    field[coord] = '('+str(i)+')'
    if i == 200:
        break
    print(i, angle, coord)
print(field)

# Write the field map to a text file
with open('field.txt', 'w') as f:
    for line in field:
        f.writelines(line)
        f.writelines('\n')
        

        
# angles = angles[order]
# distnaces = distances[order]
# coords = coords[order]

# for i in range(1,len(angles)):
#     if angles[i] == angles[i-1]:




# print(order)


# # c = cycle(

# # ast1 = angles[angles]



    


