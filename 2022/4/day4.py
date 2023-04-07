# day 4 solution
# Camp Cleanup

# list of all pairs and their section assignments
input_file = '2022/4/4.txt'
with open(input_file) as f:
    pairs = f.read().splitlines()

# count which pairs have assignments where one fully contains the other
contain = 0
# count which pairs have overlapping assignments
overlap = 0
# interate through all the pairs and count
for pair in pairs:
    first, second = pair.split(',')
    f1, f2 = first.split('-')
    s1, s2 = second.split('-')
    f1, f2, s1, s2 = [int(x) for x in [f1, f2, s1, s2]]
    if f1 <= s1 and s2 <= f2 or s1 <= f1 and f2 <= s2:
        contain += 1
    if f1 <= s1 and f2 >= s1 or s1 <= f1 and s2 >= f1:
        overlap += 1
    
# ans for part 1
print(f'part 1: {contain}')

# ans for part 2
print(f'part 2: {overlap}')
