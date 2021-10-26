class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer_len = 1
        for i in range(1, len(nums)+1):
            answer_len*=i
        answers = [[] for i in range(answer_len)]
        for num_index, num in enumerate(nums):
            index = 0
            length = answer_len
            for i in range(1, num_index+2):
                length/=i
            for answer_index, answer in enumerate(answers):
                check = answer.copy()
                check.insert(index, num)
                while answers.count(check) == length:
                    index+=1
                    if index > len(answer):
                        index = 0
                    check = answer.copy()
                    check.insert(index, num)
                answer.insert(index, num)
        return answers

      
# class Solution:
#     def __init__(self):
#         self.answer = []
        
#     def dfs(self, nums: List[int], answer) -> List[List[int]]:
#         for num in nums:
#             if num not in answer:
#                 new_answer = answer + [num]
#                 if len(new_answer) == len(nums):
#                     self.answer.append(new_answer)
#                     return
#                 self.dfs(nums, new_answer)
        
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         self.dfs(nums, [])
#         return self.answer
