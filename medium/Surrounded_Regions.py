class Solution:
    def __init__(self):
        self.width = 0
        self.length = 0
        self.queue = []
        self.safe = []
        self.safe_key = False
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.length = len(board)
        self.width = len(board[0])
        def check(i, j):
            self.queue.append((i, j))
            if i != 0:
                if board[i-1][j] == 'O' and (i-1, j) not in self.queue:
                    check(i-1, j)
            if j != 0:
                if board[i][j-1] == 'O' and (i, j-1) not in self.queue:
                    check(i, j-1)
            if i != self.length-1:
                if board[i+1][j] == 'O' and (i+1, j) not in self.queue:
                    check(i+1, j)
            if j != self.width-1:
                if board[i][j+1] == 'O' and (i, j+1) not in self.queue:
                    check(i, j+1)
                
        for i in [0, self.length-1]:
            for j in range(self.width):
                if board[i][j] != 'X':
                    check(i, j)
                    for l, w in self.queue:
                        board[l][w] = '*'
                    self.queue = []
                    
        for j in [0, self.width-1]:
            for i in range(self.length):
                if board[i][j] != 'X':
                    check(i, j)
                    for l, w in self.queue:
                        board[l][w] = '*'
                    self.queue = []
        
        for i in range(self.length):
            for j in range(self.width):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '*':
                    board[i][j] = 'O'
        return board
