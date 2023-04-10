# day 8 solution
# Treetop Tree House

from math import prod

def main():
	input_file = '2022/8/8.txt'
	try:
		with open(input_file) as f:
			tree_map = [[int(t) for t in line] for line in f.read().split()]
	except Exception as e:
		print(f"error: {e}")

	visible_trees = visibility(tree_map)
	scenic_score = max_score(tree_map)

	print(f"part 1: {visible_trees}")
	print(f"part 2: {scenic_score}")


# function for checking how many trees in the given grid are visible
# takes 2d list as arg, returns int
def visibility(grid: list) -> int:
	visible_trees = 0
	for i, row in enumerate(grid):
		for j, tree in enumerate(row):
			# checks if tree is in edge of grid
			if i == 0 or i == len(row) - 1 or j == 0 or j == len(grid) - 1:
				visible_trees += 1
				continue
			# using any() for better readability
			if any([all(tree > t for t in row[:j]), 		# left
					all(tree > t for t in row[j+1:]),		# right
					all(tree > r[j] for r in grid[:i]),		# top
					all(tree > r[j] for r in grid[i+1:])]	# bottom
				):
				visible_trees += 1

	return visible_trees


# function for finding highest scenic score possible of all trees in given grid
# takes 2d list as arg, returns int
def max_score(grid: list) -> int:
	high_score = 0
	for i, row in enumerate(grid):
		for j, tree in enumerate(row):
			score = prod([
				view(tree, grid[i][:j][::-1]),				# left
				view(tree, grid[i][j+1:]),					# right
				view(tree, [r[j] for r in grid[:i][::-1]]),	# top
				view(tree, [r[j] for r in grid[i+1:]])		# bottom
			])
			high_score = max(high_score, score)

	return high_score


def view(height: int, sight: list) -> int:
	distance = 0
	for tree in sight:
		distance += 1
		if height <= tree:
			return distance
		
	return distance


if __name__ == '__main__':
	main()
