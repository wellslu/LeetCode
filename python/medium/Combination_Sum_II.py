class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        candidates = sorted(candidates)
        def candidate_sum(candidates: List[int], combinations: List[int], target: int) -> None:
            target = target - combinations[-1]
            if target == 0:
                if combinations not in answer:
                    answer.append(combinations)
            elif target < 0:
                pass
            else:
                for digit in sorted(list(set(candidates))):
                    index = candidates.index(digit)
                    if candidates[index] > target:
                        break
                    candidate_sum(candidates[index+1:], combinations+[candidates[index]], target)
        for digit in sorted(list(set(candidates))):
            index = candidates.index(digit)
            candidate_sum(candidates[index+1:], [candidates[index]], target)
        return answer
