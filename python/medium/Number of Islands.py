class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        length = len(grid)
        width = len(grid[0])
        def next_node(i, j):
            if grid[i][j] == '1':
                grid[i][j] = '0'
            else:
                return;

            if i == 0 and j == 0:
                pass
            elif i == 0:
                next_node(i, j-1)
            elif j == 0:
                next_node(i-1, j)
            else:
                next_node(i-1, j)
                next_node(i, j-1)

            if i == length-1 and j == width-1:
                pass
            elif i == length-1:
                next_node(i, j+1)
            elif j == width-1:
                next_node(i+1, j)
            else:
                next_node(i+1, j)
                next_node(i, j+1)
        for i in range(length):
            for j in range(width):
                if grid[i][j] == '1':
                    ans+=1
                    next_node(i, j)
        return ans
