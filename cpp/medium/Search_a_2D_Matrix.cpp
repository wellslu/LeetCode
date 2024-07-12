class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();
        int j = m / 2;
        if (target < matrix[j][0]) j = find_j(matrix, target, 0, j);
        else if (target >= matrix[j][0]) j = find_j(matrix, target, j, m);

        return find_i(matrix, target, j, 0, n-1);
    }

    int find_j(vector<vector<int>>& matrix, int target, int j0, int j1) {
        if (j1 <= j0 + 1) return j0;
        int j = (j0 + j1) / 2;
        if (target < matrix[j][0]) {
            return find_j(matrix, target, j0, j);
        }
        else return find_j(matrix, target, j, j1);
    }

    bool find_i(vector<vector<int>>& matrix, int target, int j, int i0, int i1) {
        if (matrix[j][i0] == target || matrix[j][i1] == target) return true;
        else if (i1 <= i0 + 1) return false;
        int i = (i0 + i1) / 2;
        if (target < matrix[j][i]) {
            return find_i(matrix, target, j, i0, i);
        }
        else return find_i(matrix, target, j, i, i1);
    }
};
