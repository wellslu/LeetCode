class Solution {
public:
    int numTrees(int n) {
        int ans;
        int num;
        vector<int> table{1, 1, 2};
        for (int i = 3; i <= n; ++i) {
            num = 0;
            for (int j = 0; j < i; ++j) {
                num+=table[j]*table[i-1-j];
            }
            table.push_back(num);
        }
        return table[n];
    }
};
