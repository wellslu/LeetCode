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

    
    
    
    
    
    

    
    
    
    
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         length = len(matrix)
#         width = len(matrix[0])
#         matrix_dp = [[0 for j in range(width)] for i in range(length)]
#         for i in range(length):
#             if matrix[i][0] == '1':
#                 matrix_dp[i][0] = 1
#         for j in range(width):
#             if matrix[0][j] == '1':
#                 matrix_dp[0][j] = 1
#         ans = max(matrix_dp[0])
#         for i in range(1, length):
#             for j in range(1, width):
#                 if matrix[i][j] == '1':
#                     matrix_dp[i][j] = min(matrix_dp[i-1][j], matrix_dp[i][j-1], matrix_dp[i-1][j-1])+1
#             ans = max(max(matrix_dp[i]), ans)
#         return ans*ans
