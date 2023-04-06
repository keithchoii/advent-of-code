# day 7 solution
# No Space Left On Device

from collections import defaultdict
from itertools import accumulate

input_file = '2022/7/input.txt'
with open(input_file) as f:
    data = f.read().splitlines()

def scan_files(filesystem: str) -> dict:
    dirs = defaultdict(int)

    for line in filesystem:
        match line.split(' '):
            case ['$', 'cd', '/']:
                cd = ['/']
            case ['$', 'cd', '..']:
                cd.pop()
            case ['$', 'cd', dir_name]:
                # added a hyphen to names for readibility when printing dirs
                cd.append(dir_name + '-')
            case ['$', 'ls'] | ['dir', _]:
                pass
            case [size, _]:
                # accumulate makes sure duplicate directories aren't stored the same
                for d in accumulate(cd):
                    dirs[d] += int(size)
            case _:
                print(f'no match for {line}')
    
    return dirs

def part_one(filesystem: str) -> int:
    dirs = scan_files(filesystem)
    
    return sum(d for d in dirs.values() if d <= 100_000)
    
def part_two(filesystem: str) -> int:
    dirs = scan_files(filesystem)
    total_space = 70_000_000
    needed_space = 30_000_000

    return min(d for d in dirs.values() if d >= dirs['/'] - (total_space - needed_space))

if __name__ == '__main__':
    print(f'part 1: {part_one(data)}')
    print(f'part 2: {part_two(data)}')
