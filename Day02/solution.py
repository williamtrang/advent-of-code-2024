def part_1(fp: str) -> int:
    safe_reports = 0
    with open(fp) as f:
        for line in f:
            nums = line.strip().split(' ')
            nums = [int(num) for num in nums]
            num_gaps = lambda x: all([(abs(x[i] - x[i + 1]) >= 1) and \
                                      (abs(x[i] - x[i + 1]) <= 3) for i in range(len(x) - 1)])

            if (mono_increase(nums) or mono_decrease(nums)) and num_gaps(nums):
                safe_reports += 1
        
        return safe_reports

def part_2(fp):
    return

def mono_increase(lst: list[int]) -> bool:
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))

def mono_decrease(lst: list[int]) -> bool:
    return all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))

def mono_increasing_skip(lst: list[int]) -> bool:
    """
    Checks a list to see if it is monotonically increasing if at most one
    number is excluded

    Args:
        lst: list of numbers
    Returns:
        if lst is monotonically increasing with one number skipped
    Raises:

    >>> lst = [1, 3, 2, 4, 5]
    >>> mono_increasing_skip(lst)
    True
    
    >>> lst = [1, 3, 2, 2, 5]
    >>> mono_increasing_skip(lst)
    False

    >>> lst = [1, 3, 9, 4, 5]
    >>> mono_increasing_skip(lst)
    True

    >>> lst = [1, 2, 3, 4, 5]
    >>> mono_increasing_skip(lst)
    True

    >>> lst = [9, 1, 2, 3, 4]
    >>> mono_increasing_skip(lst)
    True

    >>> lst = [1, 2, 3, 4, 1]
    >>> mono_increasing_skip(lst)
    True

    >>> lst = [1, 2, 3, 1, 1, 3]
    >>> mono_increasing_skip(lst)
    False
    """

    
    i = 0
    while i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            i += 1
            continue
        else:
            lst.pop(i + 1)
            break
    return mono_increase(lst)

    """

    skipped = False
    i = 0
    while i < (len(lst) - 1):
        if lst[i] < lst[i + 1]:
            i += 1
            continue
        elif ((i + 2) < len(lst)) and not skipped and (lst[i] < lst[i + 2]):
            skipped = True
            i += 2
        else:
            return False
    return True
    """

if __name__ == '__main__':
    print(part_1('tests/input_test.txt'))
    print(part_1('input.txt'))
    #print(part_2('tests/input_test.txt'))