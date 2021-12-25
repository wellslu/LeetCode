class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        length = len(matrix)
        width = len(matrix[0])
        for i in range(length):
            for j in range(width):
                if matrix[i][j] == '1':
                    if ans > 0:
                        square = ans
                    else:
                        square = 1
                    key = True
                    while key:
                        for r in range(square+1):
                            if i+r >= length or j+square+1 > width or '0' in matrix[i+r][j:j+square+1]:
                                key = False
                                if ans < square:
                                    ans = square
                                break
                        square+=1
        return ans*ans
