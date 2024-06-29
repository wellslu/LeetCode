class Solution:
    def trailingZeroes(self, n: int) -> int:
        a = 1
        for i in range(2, n+1):
            a*=i
        ans = 0
        for i in str(a)[::-1]:
            if i == '0':
                ans+=1
            else:
                return ans
              
              
              
              
# class Solution:
#     def trailingZeroes(self, n: int) -> int:
#         ans = 0
#         for i in range(5, n+1, 5):
#             while i % 5 == 0:
#                 ans+=1
#                 i/=5
#         return ans
