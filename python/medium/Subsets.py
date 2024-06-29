class Solution:
    def __init__(self):
        self.answer = [[]]
        
        
    def next_number(self, nums, answer, cnt):
        if len(answer) == cnt:
            self.answer.append(answer)
        for index in range(len(nums)):
            self.next_number(nums[index+1:], answer+[nums[index]], cnt)
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        for r in range(1, len(nums)):
            for index in range(len(nums)):
                self.next_number(nums[index+1:], [nums[index]], r)
        self.answer.append(nums)
        return self.answer
