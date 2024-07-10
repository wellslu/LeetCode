class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        for(int j = 1; j < m; ++j) grid[j][0]+=grid[j-1][0];
        for(int i = 1; i < n; ++i) grid[0][i]+=grid[0][i-1];
        for (int j = 1; j < m; ++j) {
            for (int i = 1; i < n; ++i) {
                grid[j][i] = grid[j][i] + min(grid[j-1][i], grid[j][i-1]);
            }
        }
        return grid[m-1][n-1];
    }
};
