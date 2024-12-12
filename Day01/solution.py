def part_1(fp):
    first_list = []
    second_list = []
    distance = 0

    with open(fp) as f:
        for line in f:
            nums = line.split('   ')
            first_list.append(int(nums[0]))
            second_list.append(int(nums[1].strip()))
    
    first_list_sorted = sorted(first_list)
    second_list_sorted = sorted(second_list)

    for i in range(len(first_list_sorted)):
        distance += abs(first_list_sorted[i] - second_list_sorted[i])
    
    return distance

def part_2(fp):
    first_list = []
    second_list = []
    second_counts = {}
    sim_score = 0

    with open(fp) as f:
        for line in f:
            nums = line.split('   ')
            first_list.append(int(nums[0]))
            second_list.append(int(nums[1].strip()))
    
    for num in second_list:
        if num not in second_counts:
            second_counts[num] = 0
        second_counts[num] += 1
    
    second_keys = set(second_counts.keys())
    for num in first_list:
        if num in second_keys:
            sim_score += num * second_counts[num]
        else:
            continue

    return sim_score


if __name__ == '__main__':
    print(part_1('input.txt'))
    print(part_2('input.txt'))