class Solution {
public:
    int numDecodings(string s) {
        if (s.length() == 0 || s[0] == '0') return 0;
        vector<int> ans_list{1, 0};
        int s_int = stoi(s.substr(0, 2));;
        if (s[1] != '0') ans_list[1]++;
        if (s_int > 0 && s_int <= 26) ans_list[1]++;
        for (int i = 2; i < s.length(); ++i) {
            if (s[i] != '0') ans_list.push_back(ans_list[i-1]);
            else ans_list.push_back(0);
            s_int = stoi(s.substr(i-1, 2));
            if (s[i-1] != '0' && s_int > 0 && s_int <= 26) ans_list[i]+=ans_list[i-2];
        }
        return ans_list[s.length()-1];
    }
};
