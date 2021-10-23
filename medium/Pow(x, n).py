class Solution:
    def Pow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        elif n % 2 == 0:
            return self.Pow(x*x, abs(n)/2)
        else:
            return x*self.Pow(x*x, (abs(n)-1)/2)
    
    def myPow(self, x: float, n: int) -> float:
        # return x**n
        if n == 0:
            return 1
        answer = self.Pow(x, abs(n))
        if n > 0:
            return answer
        else:
            return 1/answer
