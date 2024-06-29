class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        s = s.split(' ')
        for w in s[::-1]:
            w = w.replace(' ', '')
            if w != '':
                ans+=w
                ans+=' '
        return ans[:-1]
