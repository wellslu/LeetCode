class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ans;
        unordered_map<string, vector<string>> mp;
        // sort(strs.begin(), strs.end());
        for (auto str:strs) {
            string s = str;
            sort(s.begin(), s.end());
            mp[s].push_back(str);
        }
        for(auto &it : mp) {
            ans.push_back(move(it.second));
        }
        return ans;

        // bool k = true;
        // for (auto str:strs) {
        //     for (int i = 0; i < ans.size(); ++i) {
        //         if (ans[i][0].length() != str.length()) 0;
        //         else if (filter(ans[i][0], str)) {
        //             ans[i].push_back(str);
        //             k = false;
        //         }
        //     }
        //     if (k) ans.push_back(vector<string>{str});
        //     else k = true;
        // }
        // return ans;
    }

    // bool filter(string s1, string s2) {
    //     for (auto s:s1) {
    //         for (int i = 0; i < s2.length(); ++i) {
    //             if (s == s2[i]) {
    //                 s2.erase(i, 1);
    //                 break;
    //             }
    //         }
    //     }
    //     if (s2.length() == 0) return true;
    //     return false;
    // }
};
