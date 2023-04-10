# day 7 solution
# No Space Left On Device

from collections import defaultdict
from itertools import accumulate

def main():
    input_file = '2022/7/7.txt'
    try:
        with open(input_file) as f:
            data = f.read().splitlines()
    except Exception as e:
        print(f"error: {e}")

    dirs = scan_files(data)
    total_space = 70_000_000
    needed_space = 30_000_000

    print(f"part 1: {sum(d for d in dirs.values() if d <= 100_000)}")
    print(f"part 2: {min(d for d in dirs.values() if d >= dirs['/'] - (total_space - needed_space))}")


# function parses through list of commands and calculates the size each directory occupies, storing the results in a dictionary
# takes list of strings as arg, returns dictionary
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
                # accumulate makes sure duplicate directories aren't stored the in same key in dirs
                for d in accumulate(cd):
                    dirs[d] += int(size)
            case _:
                print(f'no match for {line}')
    
    return dirs


if __name__ == '__main__':
    main()
