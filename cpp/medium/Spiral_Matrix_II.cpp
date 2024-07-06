class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> answer;
        for (int i = 0; i < n; i++) {
            vector<int> v = {};
            for (int j = 0; j < n; j++) {
                v.push_back(3*i+j);
            }
            answer.push_back(v);
        }

        int num = 1;
        int i = 0, r = 0;
        int count = n*n+1;
        while(true) {
            for (i = 0+r; i <= n-r-1; i++) {
                // cout << i << "," << r << "->" << num << endl;
                answer[r][i] = num;
                num++;
            }
            if (num == count) break;
            num--;
            for (i = 0+r; i <= n-r-1; i++) {
                // cout << n-1-r << "," << i << "->" << num << endl;
                answer[i][n-1-r] = num;
                num++;
            }
            if (num == count) break;
            num--;
            for (int i = n-r-1; i > r; i--) {
                // cout << i << "," << n-1-r << "->" << num << endl;
                answer[n-1-r][i] = num;
                num++;
            }
            if (num == count) break;
            for (int i = n-r-1; i >= 1+r; i--) {
                // cout << r << "," << i << "->" << num << endl;
                answer[i][r] = num;
                num++;
            }
            if (num == count) break;
            r++;
        }
        return answer;
    }
};
