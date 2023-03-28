# day 3 solution
# Rucksack Reorganization

from string import ascii_letters

# list of all rucksacks
sacks = open('2022/3/input.txt').read().splitlines()

# find priority of shared item type of each rucksack and calculate sum of all priorities
total_prio = 0
for sack in sacks:
    first, second = sack[:len(sack) // 2], sack[len(sack) // 2:]
    shared, = set(first).intersection(set(second))
    total_prio += ascii_letters.index(shared) + 1

# ans for part 1
print(f'part 1: {total_prio}')

# split the rucksacks into groups of three and find the common item
# then calculate sum of priorities of all groups
total_prio = 0
for s in range(0, len(sacks), 3):
    first, second, third = sacks[s:s + 3]
    badge, = set(first) & set(second) & set(third)
    total_prio += ascii_letters.index(badge) + 1

# ans for part 2
print(f'part 2: {total_prio}')
