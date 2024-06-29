class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        f = 1
        s = x
        while True:
            mid = int((f+s)/2)
            if mid*mid <= x and (mid+1)*(mid+1) > x:
                break
            elif mid*mid < x:
                f = mid
            else:
                s = mid
        return mid
