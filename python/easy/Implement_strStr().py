class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle is '':
            return 0
        elif len(list(needle)) > len(list(haystack)):
            return -1
        else:
            if needle in haystack:
                l = len(list(needle))
                f = len(list(haystack))
                for i in range(f-l+1):
                    if list(haystack)[i:i+l] == list(needle):
                        break
                return i
            else:
                return -1
