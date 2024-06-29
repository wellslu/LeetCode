class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        nums1 = nums.copy()
        nums1[1] = max(nums1[:2])
        for index, num in enumerate(nums1[2:-1]):
            nums1[index+2] = max(nums1[index+1], num+nums1[index+0])
        if max(nums1[-1]+nums1[-3], nums1[-2]) == nums1[-2]:
            return nums1[-2]
        nums[2] = max(nums[1:3])
        for index, num in enumerate(nums[3:]):
            nums[index+3] = max(nums[index+2], num+nums[index+1])
        # print(nums)
        return max(nums1[-2], nums[-1])
