return sum(
        any(
			# checks if tree is in edge of grid
            i == 0 or i == len(row) - 1 or j == 0 or j == len(grid) - 1 or
			# checks left, right, top, and bottom of each tree
            int(grid[i][j]) > max(
                row[j+1:], row[:j], [r[j] for r in grid[:i]], [r[j] for r in grid[i+1:]]
            )
            for j in range(len(row))
        )
        for i, row in enumerate(grid)
	)