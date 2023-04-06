# day 1 solution
# Calorie Counting

# split the input list into a new list with each item in the list representing the calories of all snacks carried by one elf
input_file = '2022/1/input.txt'
with open(input_file) as f:
    elf_list = f.read().split('\n\n')


# use sum() to add together all the snacks' calories for each elf and make a new list
# each item of the list represents the total calories one elf carries
cals_per_elf = [sum(int(cal) for cal in elf.split()) for elf in elf_list]

# ans for part 1
# use max() to find the most calories carried by one elf
print(f'part 1: {max(cals_per_elf)}')

# ans for part 2
# use sort() to find the top three elves carrying the most calories and add them together for total sum
print(f'part 2: {sum(sorted(cals_per_elf)[-3::])}')
