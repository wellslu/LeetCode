class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        set<int> x_axis;
        set<int> y_axis;
        for (int j = 0; j < m; ++j) {
            for (int i = 0; i < n; ++i) {
                if (matrix[j][i] == 0) {
                    y_axis.insert(j);
                    x_axis.insert(i);
                }
            }
        }

        for (auto y:y_axis) {
            for (int i = 0; i < n; ++i) {
                matrix[y][i] = 0;
            }
        }

        for (auto x:x_axis) {
            for (int j = 0; j < m; ++j) {
                matrix[j][x] = 0;
            }
        }
    }
};
