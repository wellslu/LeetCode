class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        answer = [[] for i in range(n)]
        num = 1
        for r in range(int(n/2+0.5)):
            x = r
            y = r
            for w in range(0, n-2*r):
                answer[y].insert(w+r, num)
                x+=1
                num+=1
            for l in range(1, n-2*r):
                y+=1
                answer[y].insert(-r, num)
                num+=1
            for w in range(1, n-2*r):
                x-=1
                answer[y].insert(r, num)
                num+=1
            for l in range(1, n-2*r-1):
                y-=1
                answer[y].insert(r, num)
                num+=1
        return answer
