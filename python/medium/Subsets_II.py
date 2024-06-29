class Solution:
    def __init__(self):
        self.answer = [[]]
    
    def next_number(self, nums, answer, cnt):
        if len(answer) == cnt:
            self.answer.append(answer)
        else:
            for num in set(nums):
                index = nums.index(num)
                self.next_number(nums[index+1:], answer+[num], cnt)
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        for r in range(1, len(nums)):
            for num in set(nums):
                index = nums.index(num)
                self.next_number(nums[index+1:], [num], r)
        self.answer.append(nums)
        return self.answer
