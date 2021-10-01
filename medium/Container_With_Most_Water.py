class Solution:
    def maxArea(self, height: List[int]) -> int:
        f = 0
        s = len(height)-1
        answer = 0
        while s > f:
            a = (s-f) * min(height[f], height[s])
            if a > answer:
                answer = a
            if height[s] >= height[f]:
                f+=1
            else:
                s-=1
        return answer
