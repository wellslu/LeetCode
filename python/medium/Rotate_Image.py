class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = 0
        n = len(matrix)-1
        while r < n/2:
            for i in range(n-r*2):
                current_point = matrix[r][r+i]
                next_point = matrix[r+i][n-r]
                matrix[r+i][n-r] = current_point
                current_point = next_point
                next_point = matrix[n-r][n-r-i]
                matrix[n-r][n-r-i] = current_point
                current_point = next_point
                next_point = matrix[n-r-i][r]
                matrix[n-r-i][r] = current_point
                current_point = next_point
                next_point = matrix[r][r+i]
                matrix[r][r+i] = current_point
            r+=1
        return matrix
