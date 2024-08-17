class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        wordList.push_back(beginWord);
        int beginint = wordList.size() - 1;
        int endint = -1;
        int diffWord;
        vector<vector<int>> matrix(wordList.size(), vector<int>(wordList.size(), 0));
        for (int j = 0; j < wordList.size(); ++j) {
            if (wordList[j] == endWord) endint = j;
            for (int i = j+1; i < wordList.size(); ++i) {
                diffWord = 0;
                for (int w = 0; w < wordList[j].size(); ++w) {
                    if (wordList[j][w] != wordList[i][w]) ++diffWord;
                    if (diffWord == 2) break;
                }
                if (diffWord == 1) {
                    matrix[j][i] = 1;
                    matrix[i][j] = 1;
                }
            }
        }
        if (endint == -1) return 0;

        int step = 1;
        while(matrix[beginint][endint] == 0 && step <= matrix.size()) {
            for (int i = 0; i < wordList.size(); ++i) {
                if (matrix[beginint][i] == step) {
                    next_step(matrix, beginint, i);
                }
            }
            step++;
        }
        if (step > matrix.size()) return 0;
        return step+1;
    }
    void next_step(vector<vector<int>>& matrix, int beginint, int nextint) {
        for (int i = 0; i < matrix.size(); ++i) {
            if (matrix[beginint][i] == 0 && matrix[nextint][i] == 1) matrix[beginint][i] = matrix[beginint][nextint] + 1;
        }
    }
};
