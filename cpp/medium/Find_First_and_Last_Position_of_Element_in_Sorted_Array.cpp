class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int length = nums.size();
        int idx = length - 1;
        vector<int> answer = {-1, -1};
        if (length == 0) return answer;
        while (target < nums[idx] and idx != 0){
            idx/=2;
        }
        if (idx == 0 and target < nums[idx]) return answer;
        if (idx == length-1 and target > nums[idx]) return answer;
        int max_idx = idx * 2;
        if (max_idx > length-1) max_idx = length - 1;
        while (idx > 0 and target == nums[idx]) idx--;
        while (idx <= max_idx and target != nums[idx]){
            idx++;
        }
        if (target == nums[idx]) answer[0] = idx;
        while (idx <= max_idx and target == nums[idx]){
            idx++;
        }
        if (idx > 0 and target == nums[idx-1]) answer[1] = idx-1;
        else answer[1] = answer[0];
        return answer;
    }
};
