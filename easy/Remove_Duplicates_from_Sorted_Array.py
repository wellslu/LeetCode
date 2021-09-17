class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_t = []+nums
        for i in range(len(num_t)-1):
            if num_t[i] == num_t[i+1]:
                nums.remove(num_t[i])
        return len(nums)
