// #include <string>

// using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length()==0) return 0;
        int begin = 0;
        int last = 1;
        int answer = 1;
        for (last=1; last < s.length(); ++last){
            for (int i=begin; i < last; ++i){
                if (s[i] == s[last]){
                    begin = i+1;
                    break;
                }
            }
            if (answer < last - begin +1) answer = last - begin +1;
        }
        return answer;
    }
};
