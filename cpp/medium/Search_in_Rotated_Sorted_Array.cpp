class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (target > nums[0]) {
            int idx = 1;
            int length = nums.size();
            while (idx < length and nums[idx] > nums[idx-1]){
                if (target == nums[idx]){
                    return idx;
                }
                idx++;
            }
        }
        else if (target < nums[0]) {
            int idx = nums.size()-1;
            while (idx > 0 and nums[idx] > nums[idx-1]){
                if (target == nums[idx]){
                    return idx;
                }
                idx--;
            }
            if (target == nums[idx]){
                    return idx;
            }
        }
        else if (target == nums[0]) {
            return 0;
        }
        return -1;
    }
};
