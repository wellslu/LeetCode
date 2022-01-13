class Solution:
    def hIndex(self, citations: List[int]) -> int:
        max_num = len(citations)
        min_num = 0
        while max_num > min_num+1:
            pivot = (max_num+min_num)//2
            if citations[-pivot] < pivot:
                max_num = pivot
            elif citations[-pivot] > pivot:
                min_num = pivot
            else:
                return pivot
        if citations[-min_num] >= min_num and citations[-min_num-1] <= min_num:
            return min_num
        else:
            return max_num
