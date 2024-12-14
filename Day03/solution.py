import re

def part_1(fp):
    pattern = "mul\([1-9]+,[1-9]+\)"
    sum = 0
    with open(fp) as f:
        for line in f:
            commands = re.findall(pattern, line)
            print(commands)
            for command in commands:
                print(command, sum)
                sum += eval(command)
    
    return sum

def mul(a, b):
    return a * b


if __name__ == '__main__':
    print(part_1('input.txt'))
    print(part_1('tests/input_test.txt'))