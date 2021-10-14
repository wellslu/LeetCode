class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = 0
        now_sum = 0
        for num in nums:
            now_sum = now_sum + num
            if answer < now_sum:
                answer = now_sum
            if now_sum < 0:
                now_sum = 0
        if answer == 0:
            return max(nums)
        return answer
