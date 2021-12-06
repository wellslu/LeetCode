class Solution:
    def __init__(self):
        self.seen = {}
        
    def connection(self, i, j):
        if (i, j) in self.seen:
            return;
        self.seen[(i, j)]=0
        if i == 0 and j == 0:
            pass
        elif i == 0:
            if self.grid[i][j-1] == '1':
                self.connection(i, j-1)
        elif j == 0:
            if self.grid[i-1][j] == '1':
                self.connection(i-1, j)
        else:
            if self.grid[i][j-1] == '1':
                self.connection(i, j-1)
            if self.grid[i-1][j] == '1':
                self.connection(i-1, j)
        if i+1 == self.length and j+1 == self.width:
            pass
        elif i+1 == self.length:
            if self.grid[i][j+1] == '1':
                self.connection(i, j+1)
        elif j+1 == self.width:
            if self.grid[i+1][j] == '1':
                self.connection(i+1, j)
        else:
            if self.grid[i+1][j] == '1':
                self.connection(i+1, j)
            if self.grid[i][j+1] == '1':
                self.connection(i, j+1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.length = len(grid)
        self.width = len(grid[0])
        island = 0
        for i in range(self.length):
            for j in range(self.width):
                if grid[i][j] == '1' and (i,j) not in self.seen:
                    island+=1
                    self.connection(i, j)
        return island
