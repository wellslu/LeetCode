class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        grid_t = [[] for i in range(len(grid[0]))]
        for row in grid:
            for column in range(len(row)):
                grid_t[column].append(row[column])
        answer = 0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                target = grid[row][column]
                row_max = max(grid[row])
                column_max = max(grid_t[column])
                growth = min([row_max, column_max])
                if target < growth:
                    answer+=(growth-target)
        return answer
