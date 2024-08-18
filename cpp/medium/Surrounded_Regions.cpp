class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int n = board.size();
        int m = board[0].size();
        vector<vector<int>> connect_edge;
        int j, i;
        for (int j = 0; j < n; ++j){
            for (int i = 0; i < m; ++i) {
                if (board[j][i] == 'O'){
                    if (j == 0 || i == 0 || j == n-1 || i == m-1) connect_edge.push_back(vector<int> {j, i});
                    else board[j][i] = '1';
                }
            }
        }

        for (int idx = 0; idx < connect_edge.size(); ++idx) {
            j = connect_edge[idx][0];
            i = connect_edge[idx][1];
            if (i > 0 && connect(board, j, i-1)) connect_edge.push_back(vector<int> {j, i-1});
            if (j > 0 && connect(board, j-1, i)) connect_edge.push_back(vector<int> {j-1, i});
            if (i < m-1 && connect(board, j, i+1)) connect_edge.push_back(vector<int> {j, i+1});
            if (j < n-1 && connect(board, j+1, i)) connect_edge.push_back(vector<int> {j+1, i});
        }

        for (int j = 0; j < n; ++j){
            for (int i = 0; i < m; ++i) {
                if (board[j][i] == '1') board[j][i] = 'X';
            }
        }
    }
    
    bool connect(vector<vector<char>>& board, int j, int i) {
        if (board[j][i] == '1') {
            board[j][i] = 'O';
            return true;
        }
        else return false;
    }
};
