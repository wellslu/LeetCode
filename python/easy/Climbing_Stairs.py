class Solution:
    def factorial(self, i):
        figue = 1
        for num in range(1, int(i+1)):
            figue*=num
        return figue
        
    def climbStairs(self, n: int) -> int:
        answer = 0
        for i in range(n+1):
            if (n-1*i) % 2 == 0:
                j = (n-1*i) / 2
                answer+=self.factorial(i+j)/self.factorial(i)/self.factorial(j)
        return int(answer)
