class Solution {
public:
    bool canJump(vector<int>& nums) {
        if (nums[0] == 0 && nums.size() != 1) return false;
        int max_idx = 1;
        int idx = 0;
        while (idx <= max_idx) {
            max_idx = max(idx+nums[idx], max_idx);
            if (max_idx >= nums.size()-1) return true;
            idx++;
        }
        return false;
    }
};
