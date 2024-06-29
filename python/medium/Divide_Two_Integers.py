class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
        divisor_gap = divisor_abs
        gap = 1
        answer = 0
        while divisor_abs <= dividend_abs:
            if divisor_gap > dividend_abs:
                divisor_gap=divisor_abs
                gap=1
                continue
            dividend_abs-=divisor_gap
            answer+=gap
            divisor_gap+=divisor_gap
            gap+=gap
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            answer = 0 - answer
            if answer < -2**31:
                answer = -2**31
        else:
            if answer > 2**31-1:
                answer = 2**31-1
        return answer
