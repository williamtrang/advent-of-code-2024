from itertools import product
from tqdm import tqdm

def part_1(fp: str) -> int:
    """
    Day 7 Part 1 of Advent of Code 2024. Takes in target
    and a list of numbers and outputs whether or not it is possible
    to achieve the target number by performing operations on the
    input list. If the target number is possible to reach, add to a
    rolling total, and return the total of all reachable targets

    Args:
        fp (string): input filepath
    Returns:
        int: total of all reachable targets

    >>> part_1('tests/test_input.txt')
    3749
    """

    total_sum = 0

    with open(fp) as f:
        for line in f:
            line_split = line.split(':')
            target = int(line_split[0])
            values = line_split[1].strip().split(' ')
            values = list(map(lambda x: int(x), values))

            if valid_target(values, target):
                total_sum += target
    return total_sum

def part_2(fp: str) -> int:
    """
    Day 7 Part 2 of Advent of Code 2024. Takes in target
    and a list of numbers and outputs whether or not it is possible
    to achieve the target number by performing operations on the
    input list. If the target number is possible to reach, add to a
    rolling total, and return the total of all reachable targets. Differs
    from part 1 by adding additional operators 

    Args:
        fp (string): input filepath
    Returns:
        int: total of all reachable targets
    
    >>> part_2('tests/test_input.txt')
    11387
    """
    
    total_sum = 0

    with open(fp) as f:
        for line in f:
            line_split = line.split(':')
            target = int(line_split[0])
            values = line_split[1].strip().split(' ')
            values = list(map(lambda x: int(x), values))

            if valid_target_concats(values, target):
                total_sum += target
    return total_sum

def valid_target(nums: list[int], target: int) -> bool:
    """
    Checks if a list of numbers can become the target number by
    performing math operations on the input list. Math operations
    include addition and multiplication

    Args:
        nums (list): list of numbers
        target (int): target number to reach
    Returns:
        bool: whether or not the list can become the target number

    >>> valid_target([19, 10], 190)
    True

    >>> valid_target([19, 10], 29)
    True

    >>> valid_target([81, 40, 27], 3267)
    True

    >>> valid_target([1, 2, 3], 100)
    False

    >>> valid_target([1], 3)
    False

    >>> valid_target([1, 2], 4)
    False
    """

    for ops in product(['+', '*'], repeat = (len(nums) - 1)):
        total = perform_list_operations(ops, nums)
        if total == target:
            return True
        
    return False

def valid_target_concats(nums: list[int], target: int) -> bool:
    """
    Checks if a list of numbers can become the target number by
    performing math operations on the input list. The math operations
    include addition, multiplication, and concatenation

    Args:
        nums (list): list of numbers
        target (int): target number to reach
    Returns:
        bool: whether or not the list can become the target number
    """

    for ops in tqdm(product(['+', '*', '||'], repeat = (len(nums) - 1))):
        total = perform_list_operations(ops, nums)
        if total == target:
            return True
        
    return False

def perform_list_operations(operations: tuple[str], nums: list[int]) -> int:
    """
    Performs mathematical operations on a list, in order, based on operations
    input

    Args:
        operations (tuple): tuple of operators
        nums (list): list of numbers to perform operations on
    Returns:
        int: total after all operations have been performed
    Raises:
        AssertionError: if operations list contains invalid operators 

    >>> perform_list_operations(('*', '+'), [5, 6, 13])
    43

    >>> perform_list_operations('*', [14, 6])
    84
    """

    valid_operations = set(['*', '+', '||'])
    assert all([op in valid_operations for op in operations])

    total = nums[0]
    for i, operation in enumerate(operations, start=1):
        if operation == '+':
            total = add(total, nums[i])
        elif operation == '*':
            total = mul(total, nums[i])
        elif operation == '||':
            total = int(concatenation(total, nums[i]))

    return total

def add(a, b):
    """
    Returns sum of two inputs a and b

    Args:
        a (num): first number
        b (num): second number
    Returns:
        num: sum of a and b

    >>> add(6, 4)
    10

    >>> add(-1, -5)
    -6

    >>> add(-6, 24)
    18
    """

    return a + b

def mul(a, b):
    """
    Returns product of two inputs a and b

    Args:
        a (num): first number
        b (num): second number
    Returns:
        num: product of a and b

    >>> mul(6, 4)
    24

    >>> mul(-1, -5)
    5

    >>> mul(-6, 24)
    -144
    """
    
    return a * b

def concatenation(a, b) -> str:
    """
    Concatenates and returns string representation of two inputs a and b

    Args:
        a: first input
        b: second input
    Returns:
        string: concatenated string of a and b

    >>> concatenation(6, 8)
    "68"

    >>> concatenation("ab", "ad")
    "abad"
    """

    return str(a) + str(b)

if __name__ == '__main__':
    print(part_1('input.txt'))
    print(part_2('input.txt'))