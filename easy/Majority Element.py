class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in set(nums):
            if nums.count(i) > n/2:
                return i
