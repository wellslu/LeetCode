class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        max_money = max(nums[0], nums[1])
        nums[2] = nums[0]+nums[2]
        for index, num in enumerate(nums[3:]):
            nums[index+3] = max(nums[index+3]+nums[index], nums[index+3]+nums[index+1])
        return max(nums[-3:])
