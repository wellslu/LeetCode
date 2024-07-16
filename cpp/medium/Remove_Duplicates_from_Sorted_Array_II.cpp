class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k = 0;
        int temp;
        bool key = false;
        for (int i = 0; i < nums.size(); ++i) {
            temp = nums[i];
            ++k;
            while (i+1 < nums.size() && nums[i+1] == temp) {
                ++i;
                if (key) {
                    nums.erase(nums.begin()+i);
                    --i;
                }
                else ++k;
                key = true;
            }
            key = false;
        }
        return k;
    }
};
