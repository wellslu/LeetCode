class Solution:
    def __init__(self):
        self.candidates = None
        self.answer = []
    
    def candidate_sum(self, combinations: List[int], target: int) -> None:
        target = target - combinations[-1]
        if target == 0:
            if sorted(combinations) not in self.answer:
                self.answer.append(sorted(combinations))
        elif target < 0:
            pass
        else:
            for digit in self.candidates:
                self.candidate_sum(combinations+[digit], target)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        for digit in candidates:
            self.candidate_sum([digit], target)
        return self.answer


# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         answer = []
#         candidates = sorted(candidates)
#         def candidate_sum(candidates: List[int], combinations: List[int], target: int) -> None:
#             target = target - combinations[-1]
#             if target == 0:
#                 if sorted(combinations) not in answer:
#                     answer.append(sorted(combinations))
#             elif target < 0:
#                 pass
#             else:
#                 for digit in candidates:
#                     if digit > target:
#                         break
#                     candidate_sum(candidates, combinations+[digit], target)
#         for index in range(len(candidates)):
#             candidate_sum(candidates[index:], [candidates[index]], target)
#         return answer
