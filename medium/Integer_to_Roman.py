class Solution:
    def intToRoman(self, num: int) -> str:
        num = str(num)[::-1]
        answer = ''
        for i in range(len(str(num))):
            number = int(num[i])
            if i == 0:
                if number <= 5:
                    if number <= 3:
                        answer=('I'*number)+answer
                    elif number == 4:
                        answer='IV'+answer
                    else:
                        answer='V'+answer
                else:
                    if number <= 8:
                        answer=('V'+'I'*(number-5))+answer
                    else:
                        answer='IX'+answer
            elif i == 1:
                if number <= 5:
                    if number <= 3:
                        answer=('X'*number)+answer
                    elif number == 4:
                        answer='XL'+answer
                    else:
                        answer='L'+answer
                else:
                    if number <= 8:
                        answer=('L'+'X'*(number-5))+answer
                    else:
                        answer='XC'+answer
            elif i == 2:
                if number <= 5:
                    if number <= 3:
                        answer=('C'*number)+answer
                    elif number == 4:
                        answer='CD'+answer
                    else:
                        answer='D'+answer
                else:
                    if number <= 8:
                        answer=('D'+'C'*(number-5))+answer
                    else:
                        answer='CM'+answer
            else:
                answer=('M'*number)+answer
        return answer
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# class Solution:
#     @staticmethod
#     def to_int_str(num):
#         c = ''
#         if num <= 5:
#             if num <= 3:
#                 c='1'*num
#             elif num == 4:
#                 c='15'
#             else:
#                 c='5'
#         else:
#             if num <= 8:
#                 c='5'+'1'*(num-5)
#             else:
#                 c='9'
#         return c
    
#     def intToRoman(self, num: int) -> str:
#         num = str(num)[::-1]
#         answer = ''
#         for i in range(len(str(num))):
#             number = self.to_int_str(int(num[i]))
#             if i == 0:
#                 number = number.replace('1', 'I')
#                 number = number.replace('5', 'V')
#                 number = number.replace('9', 'IX')
#                 answer=number+answer
#             elif i == 1:
#                 number = number.replace('1', 'X')
#                 number = number.replace('5', 'L')
#                 number = number.replace('9', 'XC')
#                 answer=number+answer
#             elif i == 2:
#                 number = number.replace('1', 'C')
#                 number = number.replace('5', 'D')
#                 number = number.replace('9', 'CM')
#                 answer=number+answer
#             else:
#                 number = number.replace('1', 'M')
#                 answer=number+answer
#         return answer
