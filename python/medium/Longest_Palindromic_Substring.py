class Solution:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        m = int(len(s)/2)
        if s[:m] == s[-m:][::-1]:
            return True
        else:
            return False
    
    def longestPalindrome(self, s: str) -> str:
        answer = s[0]
        l = len(s)
        for i in range(l):
            w = s[i]
            for u in range(i, l):
                if w == s[u]:
                    ss = s[i:u+1]
                    if len(ss) > len(answer):
                        if self.is_palindrome(ss):
                            answer = ss
        return answer
