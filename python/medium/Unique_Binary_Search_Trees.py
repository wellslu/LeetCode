class Solution:
    def numTrees(self, n: int) -> int:
        def next_step(n):
            if n == 1 or n == 0:
                return 1
            elif n == 2:
                return 2
            else:
                nums = 0
                for i in range(n//2):
                    nums+=next_step(i)*next_step(n-1-i)
                nums*=2
                if n % 2 == 1:
                    nums+=next_step(n//2)**2
                return nums
        nums = 0
        for i in range(n//2):
            nums+=next_step(i)*next_step(n-1-i)
        nums*=2
        if n % 2 == 1:
            nums+=next_step(n//2)**2
        return nums
        
        
# class Solution:
#     def numTrees(self, n: int) -> int:
#         ans_list = [1, 1]
#         ans = 0
#         for i in range(2, n+1):
#             a = 0
#             for j in range(i//2):
#                 a+=ans_list[j]*ans_list[i-j-1]
#             a*=2
#             if i % 2 == 1:
#                 a+=ans_list[i//2]**2
#             ans_list.append(a)
#         return ans_list[-1]
