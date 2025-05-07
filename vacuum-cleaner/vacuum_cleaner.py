class Solution:
    def vacuum_cleaner(self, grid, pos, instructions):
        row, col = pos

        for move in instructions:
            new_row, new_col = row, col

            if move == 'U':
                new_row -= 1
            elif move == 'D':
                new_row += 1
            elif move == 'L':
                new_col -= 1
            elif move == 'R':
                new_col += 1

            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                if grid[new_row][new_col] == 0:
                    row, col = new_row, new_col

        return [row, col]