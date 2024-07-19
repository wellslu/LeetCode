class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> answer;
        vector<int> combination;
        sort(nums.begin(), nums.end());
        dfs(nums, combination, answer);
        return answer;
    }
    void dfs(vector<int>& nums, vector<int>& combination, vector<vector<int>>& answer) {
        answer.push_back(combination);
        set<int> set_num(nums.begin(), nums.end());
        for (auto &i:set_num){
            combination.push_back(i);
            vector<int> sub_num(find(nums.begin(), nums.end(), i)+1, nums.end());
            dfs(sub_num, combination, answer);
            combination.pop_back();
        }
    }
};
