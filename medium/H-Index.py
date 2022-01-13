class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        citations = sorted(citations, reverse=True)
        if citations[0] == 0:
            return 0
        if citations[length-1] >= length:
            return length
        for l in range(length-1, 0, -1):
            if citations[l-1] >= l and citations[l] <= l:
                return l
