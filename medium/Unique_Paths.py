class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        step_list = []
        for i in range(m):
            step_list.append([])
            for j in range(n):
                if i == 0 or j == 0:
                    step_list[i].append(1)
                else:
                    step_list[i].append(step_list[i][j-1]+step_list[i-1][j])
        return step_list[m-1][n-1]
