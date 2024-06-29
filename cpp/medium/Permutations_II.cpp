class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<int> combination;
        vector<vector<int>> answer;
        dfs(nums, combination, answer);
        return answer;
    }
    void dfs(vector<int>& nums, vector<int>& combination, vector<vector<int>>& answer) {
        if (nums.size() == 1) {
            combination.push_back(nums[0]);
            answer.push_back(combination);
            combination.pop_back();
        }
        else{
            set<int> deduplicated_nums;
            for (int i = 0; i < nums.size(); ++i) {
                deduplicated_nums.insert(nums[i]);
            }
            for (auto i:deduplicated_nums){
                combination.push_back(i);
                vector<int> sub_nums;
                int t = i;
                for (int n = 0; n < nums.size(); ++n) {
                    if (nums[n] != t) sub_nums.push_back(nums[n]);
                    else t = 11;
                }
                dfs(sub_nums, combination, answer);
                combination.pop_back();
            }
        }
    }
};
