def part_1(fp: str) -> int:
    """
    Day 8 Part 1 of Advent of Code 2024. Takes in a map
    with antenna on the map and outputs the number of
    unique locations for antinodes between the antenna

    Args:
        fp (string): input filepath
    
    Returns:
        int: number of unique antinode locations

    >>> part_1('tests/input_test.txt')
    14
    """ 

    antenna_locations = {}
    full_map = []
    num_antinodes = 0

    with open(fp) as f:
        full_map = f.readlines()
    
    # mark all antenna locations
    for i in range(len(full_map)):
        full_map[i] = full_map[i].strip()
        for j in range(len(full_map[i])):
            if full_map[i][j] != '.':
                if full_map[i][j] not in antenna_locations:
                    antenna_locations[full_map[i][j]] = []
                antenna_locations[full_map[i][j]].append((i, j))
    
    map_dims = (len(full_map) - 1, len(full_map[0]) - 1)
    occupied_locations = set([])

    for _, v in antenna_locations.items():
        antinodes = find_antinodes(v)
        for antinode in antinodes:
            if (not out_of_bounds(antinode, map_dims)) and (antinode not in occupied_locations):
                occupied_locations.add(antinode)
                num_antinodes += 1
    
    return num_antinodes

def part_2(fp: str) -> int:
    """
    Day 8 Part 2 of Advent of Code 2024. Takes in a map
    with antenna on the map and outputs the number of unique
    locations for antinodes between the antenna, with more
    than one antinode per pair of antenna being acceptable

    Args:
        fp (string): input filepath
    
    Returns:
        int: number of unique antinode locations

    >>> part_2('tests/input_test.txt')
    34

    >>> part_2('tests/input_test_2.txt')
    9
    """

    antenna_locations = {}
    full_map = []
    num_antinodes = 0

    with open(fp) as f:
        full_map = f.readlines()
    
    # mark all antenna locations
    for i in range(len(full_map)):
        full_map[i] = full_map[i].strip()
        for j in range(len(full_map[i])):
            if full_map[i][j] != '.':
                if full_map[i][j] not in antenna_locations:
                    antenna_locations[full_map[i][j]] = []
                antenna_locations[full_map[i][j]].append((i, j))
    
    map_dims = (len(full_map) - 1, len(full_map[0]) - 1)
    occupied_locations = set([])

    for _, v in antenna_locations.items():
        antinodes = find_all_antinodes(v, map_dims)
        for antinode in antinodes:
            if antinode not in occupied_locations:
                occupied_locations.add(antinode)
                num_antinodes += 1
    
    return num_antinodes

def find_antinodes(points: list) -> list:
    """
    Finds antinodes from a list of points. Each antinode

    >>> res = find_antinodes([(4, 3), (5, 5), (8, 4)])
    >>> set(res) == set([(3, 1), (6, 7), (2, 6), (0, 2), (11, 3), (12, 5)])
    True
    """
    antinodes = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            antinodes.extend(calc_antinodes(points[i], points[j]))

    return antinodes
    
def find_all_antinodes(points: list, map_dims: tuple) -> list:

    antinodes = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            antinodes.extend(calc_all_antinodes(points[i], points[j], map_dims))

    return antinodes

def calc_antinodes(a: tuple, b: tuple) -> list:
    """
    Calculate the possible antinodes between two points a and b

    Args:
        a (tuple): first point
        b (tuple): second point
    
    Returns:
        list: list of possible antinodes for the two input points

    >>> calc_antinodes((4, 3), (5, 5))
    [(3, 1), (6, 7)]
    """
    antinodes = []
    distance = subtract_tups(a, b)

    a1 = add_tups(a, distance)
    b1 = add_tups(b, distance)
    a2 = subtract_tups(a, distance)
    b2 = subtract_tups(b, distance)

    antinodes = [x for x in [a1, b1, a2, b2] if (x != a) and (x != b)]

    return antinodes

def calc_all_antinodes(a: tuple, b: tuple, map_dims: tuple) -> list:
    """
    Calculates all possible antinodes between points a and b,
    allowing for more than two within the line. Antinodes are generated
    until one is out of the boundaries of the map

    Args:
        a (tuple): first point
        b (tuple): second point
        map_dims (tuple): dimensions of map
    
    Returns:
        list: list of all possible antinodes between two points that
        fit within map dimensions

    >>>
    
    """
    antinodes = set([])
    distance = subtract_tups(a, b)

    a1 = a
    while not out_of_bounds(a1, map_dims):
        antinodes.add(a1)
        a1 = add_tups(a1, distance)
    
    a1 = a
    while not (out_of_bounds(a1, map_dims)):
        antinodes.add(a1)
        a1 = subtract_tups(a1, distance)

    return list(antinodes)

def out_of_bounds(point: tuple, map_dims: tuple) -> bool:
    """
    Determines whether a point is out of the boundaries of
    a map with given dimensions

    Args:
        point (tuple): point to determine in or out of bounds
        map_dims (tuple): dimensions of map
    
    Returns:
        bool: whether or not the point is within the map
    
    >>> out_of_bounds((3, 1), (10, 10))
    False

    >>> out_of_bounds((12, 5), (10, 10))
    True

    >>> out_of_bounds((10, 10), (10, 10))
    False

    >>> out_of_bounds((5, 12), (10, 10))
    True

    >>> out_of_bounds((-1, 0), (1, 1))
    True
    """

    return (point[0] > map_dims[0]) or (point[1] > map_dims[1]) or (point[0] < 0) or (point[1] < 0)

def add_tups(a, b) -> tuple:
    """
    Adds two iterables of numbers and returns the
    result as a tuple

    Args:
        a: first iterable of numbers
        b: second iterable of numbers

    Returns:

    """

    assert len(a) == len(b)

    res = []
    for i in range(len(a)):
        res.append(a[i] + b[i])

    return tuple(res)

def subtract_tups(a, b) -> tuple:
    assert len(a) == len(b)

    res = []
    for i in range(len(a)):
        res.append(a[i] - b[i])

    return tuple(res)

if __name__ == '__main__':
    print(part_1('tests/input_test.txt'))
    print(part_1('input.txt'))
    print(part_2('tests/input_test_2.txt'))
    print(part_2('input.txt'))