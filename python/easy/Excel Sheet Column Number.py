class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        index = 0
        for i in columnTitle[::-1]:
            ans+=(ord(i)-64)*(26**index)
            index+=1
        return ans
