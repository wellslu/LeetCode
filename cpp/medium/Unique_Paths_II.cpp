class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        if (obstacleGrid[0][0] == 1) obstacleGrid[0][0] = 0;
        else obstacleGrid[0][0] = 1;
        
        for(int j = 1; j < m; ++j) {
            if (obstacleGrid[j][0] == 1 || obstacleGrid[j-1][0] == 0) obstacleGrid[j][0] = 0;
            else obstacleGrid[j][0] = 1;
        }
        for(int i = 1; i < n; ++i) {
            if (obstacleGrid[0][i] == 1 || obstacleGrid[0][i-1] == 0) obstacleGrid[0][i] = 0;
            else obstacleGrid[0][i] = 1;
        }

        for(int j = 1; j < m; ++j) {
            for(int i = 1; i < n; ++i) {
                if (obstacleGrid[j][i] == 1) obstacleGrid[j][i] = 0;
                else obstacleGrid[j][i] = obstacleGrid[j-1][i] + obstacleGrid[j][i-1];
            }
        }
        return obstacleGrid[m-1][n-1];
    }
};
