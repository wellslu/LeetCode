class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = -1
        while abs(index) <= len(digits) and digits[index] == 9:
            digits[index] = 0
            index-=1
        if abs(index) > len(digits):
            digits = [1] + digits
        else:
            digits[index]+=1
        return digits
