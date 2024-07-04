class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int length = matrix.size();
        int width = matrix[0].size();
        int count = length * width;
        vector<int> answer;
        int i = 0, j = 0, r = 0;
        while (true){
            while (i+r < width) {
                answer.push_back(matrix[j][i]);
                i++;
            }
            if (answer.size() == count) break;
            i--;
            j++;
            while (j+r < length) {
                answer.push_back(matrix[j][i]);
                j++;
            }
            if (answer.size() == count) break;
            j--;
            i--;
            while (i-r >= 0) {
                answer.push_back(matrix[j][i]);
                i--;
            }
            if (answer.size() == count) break;
            i++;
            j--;
            while (j-r >= 1) {
                answer.push_back(matrix[j][i]);
                j--;
            }
            if (answer.size() == count) break;
            i++;
            j++;
            r++;
        }
        return answer;
    }
};
