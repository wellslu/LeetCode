class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = left
        index = 0
        while 2**index < right-left:
            ans = ans&(left+2**index)
            index+=1
        return ans&right
