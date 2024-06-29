class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ''
        while columnNumber > 26:
            num = columnNumber%26
            if num == 0:
                num = 26
                columnNumber-=1
            ans = chr(num+64) + ans
            columnNumber = columnNumber // 26
        ans = chr(columnNumber+64) + ans
        return ans
