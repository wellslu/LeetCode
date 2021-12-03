class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if len(nums) == 1 or k == 0:
            return nums
        first, second = nums[-k:], nums[:-k]
        nums[:k] = first
        nums[k:] = second
