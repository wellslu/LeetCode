class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        bool answer = false;
        for (int j = 0; j < board.size(); ++j) {
            for (int i = 0; i < board[0].size(); ++i){
                cout << board[j][i] << endl;
                if (board[j][i] == word[0]) answer = dfs(board, word, i, j);
                if (answer) return answer;
            }
        }
        return answer;
    }
    bool dfs(vector<vector<char>>& board, string word, int i, int j) {
        if (word[0] != board[j][i]) return false;
        else if (word.size() == 1) return true;
        char temp = board[j][i];
        board[j][i] = '0';
        if (i != 0 && board[j][i-1] != '0') {
            if (dfs(board, word.substr(1, word.size()-1), i-1, j)) return true;
        };
        if (i != board[0].size()-1 && board[j][i+1] != '0') {
            if (dfs(board, word.substr(1, word.size()-1), i+1, j)) return true;
        };
        if (j != 0 && board[j-1][i] != '0') {
            if (dfs(board, word.substr(1, word.size()-1), i, j-1)) return true;
        };
        if (j != board.size()-1 && board[j+1][i] != '0') {
            if (dfs(board, word.substr(1, word.size()-1), i, j+1)) return true;
        };
        board[j][i] = temp;
        return false;
    }
};
