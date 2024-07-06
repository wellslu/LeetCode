class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        // init 0 vector[n][n]
        vector<vector<int>> answer(n, vector<int>(n));

        int num = 1;
        int i = 0, r = 0;
        int count = n*n+1;
        for(int r = 0; r <= n / 2; r++) {
            for (i = 0+r; i <= n-r-1; i++) {
                answer[r][i] = num;
                num++;
            }
            num--;
            for (i = 0+r; i < n-r-1; i++) {
                answer[i][n-1-r] = num;
                num++;
            }
            for (int i = n-r-1; i > r; i--) {
                answer[n-1-r][i] = num;
                num++;
            }
            for (int i = n-r-1; i >= 1+r; i--) {
                answer[i][r] = num;
                num++;
            }
        }
        return answer;
    }
};
