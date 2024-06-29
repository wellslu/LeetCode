class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer_list = []
        answer = 0
        for w in s:
            if w not in answer_list:
                answer_list.append(w)
            else:
                if len(answer_list) > answer:
                    answer = len(answer_list)
                answer_list = answer_list[answer_list.index(w)+1:] + [w]
        if len(answer_list) > answer:
                answer = len(answer_list)
        return answer
