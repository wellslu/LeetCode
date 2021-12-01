class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        if numerator % denominator == 0:
            return str(numerator/denominator)[:-2]
        if numerator < 0 and denominator > 0 or numerator > 0 and denominator < 0:
            negative = '-'
        else:
            negative = ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        ans = str(numerator//denominator)+'.'
        num = ''
        numerator = numerator%denominator*10
        seen = {}
        while numerator % denominator != 0:
            seen[numerator] = numerator//denominator
            num+=str(seen[numerator])
            numerator = numerator%denominator*10
            if numerator in seen:
                copy_num = ''
                while True:
                    copy_num+=str(numerator//denominator)
                    numerator = numerator%denominator*10
                    if copy_num == num[0-len(copy_num):]:
                        return negative+ans+num.replace(copy_num, '('+copy_num+')')
                    
        ans+=num
        ans+=str(numerator/denominator)
        return negative+ans[:-2]
