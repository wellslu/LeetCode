class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        answer = 0
        while s[-1] == ' ':
            s = s[:-1]
        for w in s[::-1]:
            if w == ' ':
                break
            answer+=1
        return answer
