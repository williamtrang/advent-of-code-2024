def part_1(fp: str) -> int:
    """
    
    >>> part_1('tests/input_test.txt')
    41

    >>> part_1('tests/test2.txt')
    7
    """

    full_map = []

    with open(fp) as f:
        full_map = f.readlines()
    

    start_pos = ()
    obstacles = []
    visited = []

    map_dimensions = (len(full_map), len(full_map[i]))

    for i in range(len(full_map)):
        for j in range(len(full_map[i])):
            if full_map[i][j] == '#':
                obstacles.append((i, j))
            elif full_map[i][j] == '^':
                start_pos = (i, j)
    
    return (start_pos, obstacles)

class Guard:
    def __init__(self, start_pos: tuple):
        self.current_pos = start_pos
        self.facing_direction = "up"
    
    def next_direction(self):
        if self.get_facing_direction() == "up":
            self.set_facing_direction("right")

        elif self.get_facing_direction() == "right":
            self.set_facing_direction("down")

        elif self.get_facing_direction() == "down":
            self.set_facing_direction("left")

        else:
            self.set_facing_direction("up")
    
    def set_facing_direction(self, direction: str):
        """
        Setter method for facing direction

        Args:
            direction: new facing direction
        """

        self.facing_direction = direction
    
    def get_facing_direction(self) -> str:
        """
        Getter method for facing direction

        Returns:
            facing direction of guard
        """

        return self.facing_direction

    def get_current_pos(self) -> tuple:
        """
        Getter method for current position of the guard

        Returns:
            current position of guard
        """
        
        return self.current_pos

if __name__ == '__main__':
    print(part_1('tests/input_test.txt'))