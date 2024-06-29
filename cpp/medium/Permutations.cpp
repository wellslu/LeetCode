class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> answer;
        vector<int> permutation;
        layer(nums, permutation, answer);
        return answer;
    }
    void layer(vector<int>& nums, vector<int>& permutation, vector<vector<int>>& answer) {
        if (nums.size() == 1) {
            permutation.push_back(nums[0]);
            answer.push_back(permutation);
            permutation.pop_back();
        }
        else{
            for (int i = 0; i < nums.size(); ++i) {
                permutation.push_back(nums[i]);
                vector<int> sub_nums;
                for (int n = 0; n < nums.size(); ++n) {
                    if (i != n) sub_nums.push_back(nums[n]);
                }
                layer(sub_nums, permutation, answer);
                permutation.pop_back();
            }
        }
    }
};
