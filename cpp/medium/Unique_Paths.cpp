class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> grid(m, vector<int>(n, 1));
        for(int j = 1; j < m; ++j) {
            for(int i = 1; i < n; ++i) {
                grid[j][i] = grid[j-1][i] + grid[j][i-1];
            }
        }
        return grid[m-1][n-1];
    }
};
