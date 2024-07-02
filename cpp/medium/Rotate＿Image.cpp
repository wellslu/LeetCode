class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int end = matrix[0].size() - 1;
        int temp;
        int c1;
        int c2;
        int c3;
        int c4;
        int step;
        for (int i = 0; i <= end; ++i){
            step = 0;
            while(step < end - i*2) {
                c1 = matrix[i][i+step];
                c2 = matrix[i+step][end-i];
                c3 = matrix[end-i][end-i-step];
                c4 = matrix[end-i-step][i];
                cout << i << ", " << step << endl;
                cout << c1 << ", " << c2 << ", " << c3 << ", " << c4 << endl;
                matrix[i][i+step] = c4;
                matrix[i+step][end-i] = c1;
                matrix[end-i][end-i-step] = c2;
                matrix[end-i-step][i] = c3;
                ++step;
            }
        }
        // return matrix;
    }
};
