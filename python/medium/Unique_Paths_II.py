class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        step_list = []
        for i in range(len(obstacleGrid)):
            step_list.append([])
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    step_list[i].append(0)
                elif i == 0:
                    if j != 0 and step_list[i][j-1] == 0:
                        step_list[i].append(0)
                    else:
                        step_list[i].append(1)
                elif j == 0:
                    if i != 0 and step_list[i-1][j] == 0:
                        step_list[i].append(0)
                    else:
                        step_list[i].append(1)
                else:
                    step_list[i].append(step_list[i-1][j]+step_list[i][j-1])
        return step_list[-1][-1]
