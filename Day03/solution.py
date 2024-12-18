import re

def part_1(fp):
    """
    Day 3 Part 1 of Advent of Code 2024. Takes in "corrupted memory"
    and outputs the sum of all mul commands in the memory.

    Args:
        fp: input filepath
    Returns:
        sum of all mul commands

    >>> part_1('tests/input_test.txt')
    161
    """

    pattern = r"mul\(\d+,\d+\)"
    sum = 0

    with open(fp) as f:
        for line in f:
            commands = re.findall(pattern, line)
            for command in commands:
                sum += eval(command)
    
    return sum

def mul(a, b):
    """
    Returns product of two inputs a and b

    Args:
        a: first number
        b: second number
    Returns:
        product of a and b

    >>> mul(6, 4)
    24

    >>> mul(-1, -5)
    5

    >>> mul(-6, 24)
    -144
    """
    return a * b

def part_2(fp):
    """
    Day 3 Part 2 of Advent of Code 2024. Takes in "corrupted memory"
    and outputs the sum of all mul commands, taking into account "do"
    and "don't" commands.
    
    >>> part_2('tests/input_test.txt')
    48
    """

    # regex patterns
    dont_pattern = r"don't\(\)"
    do_pattern = r"do\(\)"
    mul_pattern = r"mul\(\d+,\d+\)"

    sum = 0
    all_commands = ""

    # reading input and joining into one string
    with open(fp) as f:
        all_commands = f.readlines()
    
    all_commands = "".join(all_commands)
    all_commands = re.split(dont_pattern, all_commands)

    # default functionality is do, so calculate for first section
    first_line_muls = re.findall(mul_pattern, all_commands[0])
    for muls in first_line_muls:
        sum += eval(muls)
    
    all_commands.pop(0)

    for command in all_commands:
        search = re.search(do_pattern, command)
        if search:
            # run mul commands after do() command
            mul_commands = re.findall(mul_pattern, command[search.start():])
            for mul_command in mul_commands:
                sum += eval(mul_command)
    
    return sum

if __name__ == '__main__':
    print(part_1('input.txt'))
    print(part_2('input.txt'))
