def part_1(fp):
    safe_reports = 0
    with open(fp) as f:
        for line in f:
            nums = line.strip().split(' ')
            nums = [int(num) for num in nums]
            mono_increase = lambda x: all(x[i] < x[i + 1] for i in range(len(x) - 1))
            mono_decrease = lambda x: all(x[i] > x[i + 1] for i in range(len(x) - 1))

            num_gaps = lambda x: all([(abs(x[i] - x[i + 1]) >= 1) and (abs(x[i] - x[i + 1]) <= 3) for i in range(len(x) - 1)])

            if (mono_increase(nums) or mono_decrease(nums)) and num_gaps(nums):
                safe_reports += 1
        
        return safe_reports

if __name__ == '__main__':
    print(part_1('input_test.txt'))
    print(part_1('input.txt'))