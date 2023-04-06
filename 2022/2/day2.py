# day 2 solution
# Rock Paper Scissors

# format input list to remove spaces
input_file = '2022/2/input.txt'
with open(input_file) as f:
    guide = f.read().replace(' ', '').splitlines()

# all posible outcomes of encrypted rock paper scissors
encrypted = {
    'BX': 1,
    'CY': 2,
    'AZ': 3,
    'AX': 4,
    'BY': 5,
    'CZ': 6,
    'CX': 7,
    'AY': 8,
    'BZ': 9
}

# all possible outcomes of decoded rock paper scissors
decoded = {
    'BX': 1,
    'CX': 2,
    'AX': 3,
    'AY': 4,
    'BY': 5,
    'CY': 6,
    'CZ': 7,
    'AZ': 8,
    'BZ': 9
}

# ans for part 1
print(f'part 1: {sum(encrypted[round] for round in guide)}')

# ans for part 2
print(f'part 2: {sum(decoded[round] for round in guide)}')
