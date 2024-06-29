class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<int>> index_list;
        int i = 0, j = 0, num = 0;
        for (j=0; j < 9; ++j){
            for (i=0; i < 9; ++i){
                if (board[j][i] != '.'){
                    for (int n=0; n < num; ++n){
                        if (board[j][i] == index_list[n][0] and (i == index_list[n][1] or j == index_list[n][2] or i/3+j/3*3 == index_list[n][3])) return false;
                    }
                    index_list.push_back({board[j][i], i, j, i/3+j/3*3});
                    ++num;
                }
            }
        }
        return true;
    }
};
