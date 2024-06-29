class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        else:
            while val in nums:
                nums.remove(val)
            return len(nums)
