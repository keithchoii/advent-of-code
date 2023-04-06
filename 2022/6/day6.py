# day 6 solution
# Tuning Trouble

input_file = '2022/6/input.txt'
with open(input_file) as f:
    signal = f.read()

def start_marker(data: str, size: int) -> int:
    for i in range(size, len(data)):
        window = data[i-size:i]
        if len(set(window)) == size:
            return i

if __name__ == '__main__':
    print(f'part 1: {start_marker(signal, 4)}')
    print(f'part 2: {start_marker(signal, 14)}')
