class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> answer;
        vector<int> combination;
        dfs(nums, answer, combination);
        return answer;
    }
    void dfs(vector<int>& nums, vector<vector<int>>& answer, vector<int>& combination) {
        answer.push_back(combination);
        for(int i = 0; i < nums.size(); ++i) {
            combination.push_back(nums[i]);
            vector<int> sub_nums(nums.begin() + i + 1, nums.end());
            dfs(sub_nums, answer, combination);
            combination.pop_back();
        }
    }
};
