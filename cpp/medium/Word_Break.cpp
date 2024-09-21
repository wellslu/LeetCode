class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp(s.length()+1, false);
        dp[0] = true;
        for (int start = 0; start < s.length(); start++) {
            if (dp[start]) {
                for (auto word:wordDict) {
                    if (start+word.length() <= s.length()){
                            if (s.substr(start, word.length()) == word) {
                                dp[start+word.length()] = true;
                            }
                        }
                    }
                }
        }
        return dp[dp.size()-1];
    }
};
