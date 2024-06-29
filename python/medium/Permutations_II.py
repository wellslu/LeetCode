class Solution:
    def __init__(self):
        self.answer = []
        self.length = None
    
    def dsf(self, nums: List[int], answer: List[int]) -> List[List[int]]:
        for num in set(nums):
            index = nums.index(num)
            new_answer = answer + [num]
            if len(new_answer) == self.length and new_answer not in self.answer:
                self.answer.append(new_answer)
                return
            self.dsf(nums[:index]+nums[index+1:], new_answer)
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.length = len(nums)
        self.dsf(nums, [])
        return self.answer
