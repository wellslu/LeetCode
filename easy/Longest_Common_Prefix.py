class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        strs = sorted(strs, key=len)
        ans = ''
        ans_t = strs[0]
        num = len(list(ans_t))
        key = 0
        for ind in range(num):
            a = ans_t[ind]
            for each in strs[1:]:
                if a != each[ind]:
                    key = 1
                    break
            if key == 1:
                break
            ans = ans + a
        return ans
