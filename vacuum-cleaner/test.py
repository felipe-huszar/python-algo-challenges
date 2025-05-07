from vacuum_cleaner import Solution

grid = [
  [0, 1, 0, 0],
  [0, 1, 0, 0],
  [0, 0, 1, 0]
]
pos = [0, 0]
instructions = "DRDR"

solution = Solution()
print(solution.vacuum_cleaner(grid, pos, instructions))