class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums.count(0) == 0 or len(nums) == 1:
            return True
        target_index = 0
        while target_index < len(nums):
            while nums[target_index] != 0 and target_index < len(nums)-1:
                target_index+=1
            k = target_index
            for i, num in enumerate(nums[:target_index][::-1]):
                i+=1
                if num > i or num == i and target_index == len(nums)-1:
                    break
                else:
                    k-=1
            if k == 0:
                return False
            target_index+=1
        return True
