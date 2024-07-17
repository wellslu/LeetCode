class Solution {
public:
    bool search(vector<int>& nums, int target) {
        if (nums.size() == 1) {
            if (target == nums[0]) return true;
            else return false;
        }
        return find_t(nums, target, 0, nums.size()-1);
    }
    bool find_t(vector<int>& nums, int target, int i, int j) {
        if (target == nums[i] || target == nums[(j+i)/2] || target == nums[j]) return true;
        else if (j-i <= 1) return false;
        else if (target > nums[i] && target > nums[(j+i)/2]) return find_t(nums, target, i+1, j-1);
        else if (target < nums[i] && target > nums[(j+i)/2]) return find_t(nums, target, (j+i)/2, j);
        else if (target > nums[i] && target < nums[(j+i)/2]) return find_t(nums, target, i, (j+i)/2);
        else if (target < nums[i] && target < nums[(j+i)/2]) return find_t(nums, target, i+1, j-1);
        return false;
    }
};

// class Solution {
// public:
//     bool search(vector<int>& nums, int target) {
//         if (target >= nums[0]) {
//             for(int i = 0; i < nums.size(); ++i) {
//                 if (target == nums[i]) return true;
//             }
//         }
//         else {
//             for(int i = nums.size()-1; i >= 0; --i) {
//                 if (target == nums[i]) return true;
//             }
//         }
//         return false;
//     }
// };
