class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

      
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         answer = ''
#         a_num = 0
#         b_num = 0
#         for i, num in enumerate(a[::-1]):
#             a_num+=((2**i)*int(num))
#         for i, num in enumerate(b[::-1]):
#             b_num+=((2**i)*int(num))
#         nums = a_num + b_num
#         index = 0
#         while 2**(index+1) <= nums:
#             index+=1
#         while nums != 0:
#             if 2**index <= nums:
#                 answer+='1'
#                 nums-=2**index
#             else:
#                 answer+='0'
#             index-=1
#         for i in range(index+1):
#             answer+='0'
#         return answer
