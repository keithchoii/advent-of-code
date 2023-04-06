# day 5 solution
# Supply Stacks

import re, functools

# split input into the starting stacks and the following rearrangement procedures
input_file = '2022/5/input.txt'
with open(input_file) as f:
    stacks, moves = f.read().split('\n\n')

# parse starting stacks
stacks = [line[1::4] for line in stacks.split('\n')[::-1]]

# create stack data structure for each stack using list of lists
crates = [[crate for crate in list(stack) if crate != ' '] for stack in zip(*stacks)]

# use regex to parse rearrangement procedures and follow procedures
for move in moves.split('\n'):
    quantity, start, end = map(int, re.findall(r'\d+', move))
    for _ in range(quantity):
        crates[end - 1].append(crates[start - 1].pop())

# ans for part 1
print(f'part 1: {"".join(crate[-1] for crate in crates)}')

# follow procedures for the CrateMover 9001
newcrates = [[crate for crate in list(stack) if crate != ' '] for stack in zip(*stacks)]
for move in moves.split('\n'):
    quantity, start, end = map(int, re.findall(r'\d+', move))
    newcrates[end - 1].extend(newcrates[start - 1][-quantity:])
    newcrates[start - 1] = newcrates[start - 1][:-quantity]

# ans for part 2
print(f'part 2: {"".join(crate[-1] for crate in newcrates)}')
