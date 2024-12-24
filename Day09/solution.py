def part_1(fp): 
    """
    
    >>> part_1('tests/input_test.txt')
    1928
    """

    disk = []
    disk_size = 0
    free_space_indices = []
    file_indices = []
    disk_map = 0

    with open(fp) as f:
        disk_map = f.readlines()
    
    # input processing
    disk_map = ''.join(disk_map).strip()
    files = disk_map[::2]
    free_space = disk_map[1::2]

    files = [int(x) for x in files]
    free_space = [int(x) for x in free_space]
    
    # create disk list and track indices
    for i in range(len(free_space)):
        disk.extend([i] * files[i])
        file_indices.extend(range(disk_size, disk_size + files[i]))
        disk_size += files[i]

        disk.extend(['.'] * free_space[i])
        free_space_indices.extend(range(disk_size, disk_size + free_space[i]))
        disk_size += free_space[i]

    # odd number contingency
    if len(files) > len(free_space):
        disk.extend([len(free_space)] * files[-1])
        file_indices.extend(range(disk_size, disk_size + files[-1]))

    # swap files and free space
    file_indices_rev = file_indices[::-1]
    for i in range(min(len(file_indices), len(free_space_indices))):
        if file_indices_rev[i] < free_space_indices[i]:
            break
        
        disk[free_space_indices[i]] = disk[file_indices_rev[i]]
        disk[file_indices_rev[i]] = '.'
        
    checksum = 0
    for i, val in enumerate(disk):
        if val == '.':
            break
        checksum += val * i
    
    return checksum

def part_2(fp):
    """
    
    >>> part_2('tests/input_test.txt')
    2858
    """

    disk = []
    disk_size = 0
    free_space_indices = []
    file_indices = []
    disk_map = 0

    with open(fp) as f:
        disk_map = f.readlines()
    
    # input processing
    disk_map = ''.join(disk_map).strip()
    files = disk_map[::2]
    free_space = disk_map[1::2]

    files = [int(x) for x in files]
    free_space = [int(x) for x in free_space]
    


    for i in range(len(free_space)):
        disk.extend([i] * files[i])
        file_indices.extend(range(disk_size, disk_size + files[i]))
        disk_size += files[i]

        disk.extend(['.'] * free_space[i])
        free_space_indices.extend(range(disk_size, disk_size + free_space[i]))
        disk_size += free_space[i]

    if len(files) > len(free_space):
        disk.extend([len(free_space)] * files[-1])
        file_indices.extend(range(disk_size, disk_size + files[-1]))

    file_indices_rev = file_indices[::-1]
    for i in range(min(len(file_indices), len(free_space_indices))):
        if file_indices_rev[i] < free_space_indices[i]:
            break
        
        disk[free_space_indices[i]] = disk[file_indices_rev[i]]
        disk[file_indices_rev[i]] = '.'
        
    checksum = 0
    for i, val in enumerate(disk):
        if val == '.':
            continue
        checksum += val * i
    
    return checksum

if __name__ == '__main__':
    #print(part_1('tests/input_test.txt'))
    print(part_1('input.txt'))