class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for query in queries:
            cnt = 0
            x1, y1, r = query
            for point in points:
                if r >= (abs(x1 - point[0])**2 + abs(y1 - point[1])**2) ** 0.5:
                    cnt+=1
            answer.append(cnt)
        return answer
