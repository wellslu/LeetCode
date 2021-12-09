class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        ans = len(nums)
        index = 0
        queue = 0
        queue_sum = 0
        for num in nums:
            queue+=1
            queue_sum+=num
            if queue_sum >= target:
                while queue_sum >= target:
                    queue_sum-=nums[index]
                    index+=1
                    queue-=1
                ans = min(ans, queue+1)
        return ans
