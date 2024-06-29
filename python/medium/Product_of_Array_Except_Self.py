class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]
        for i, n in enumerate(nums[::-1]):
            answer.append(answer[i]*n)
        answer = answer[:-1][::-1]
        a = 1
        for i, n in enumerate(nums[:-1]):
            answer[i] = answer[i]*a
            a = a*n
        answer[-1] = answer[-1]*a
        return answer
