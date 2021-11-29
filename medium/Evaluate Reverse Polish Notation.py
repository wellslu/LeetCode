class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        digits = [str(i) for i in range(10)]
        operators = ['+', '-', '*', '/']
        while '+' in tokens or '-' in tokens or '*' in tokens or '/' in tokens:
            for index, operator in enumerate(tokens):
                if operator in operators:
                    tokens.pop(index)
                    num2 = tokens.pop(index-1)
                    num1 = tokens.pop(index-2)
                    if operator == '+':
                        tokens.insert(index-2, int(num1)+int(num2))
                    elif operator == '-':
                        tokens.insert(index-2, int(num1)-int(num2))
                    elif operator == '*':
                        tokens.insert(index-2, int(num1)*int(num2))
                    else:
                        tokens.insert(index-2, int(num1)/int(num2))
                    break
        return int(tokens[0])
      
      
      
      
      
      
      
      
      
# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []
#         digits = [str(i) for i in range(10)]
#         for num in tokens:
#             if num[-1] in digits:
#                 stack.append(int(num))
#             else:
#                 num2 = stack.pop()
#                 num1 = stack.pop()
#                 if num == '+':
#                     stack.append(num1+num2)
#                 elif num == '-':
#                     stack.append(num1-num2)
#                 elif num == '*':
#                     stack.append(int(num1*num2))
#                 else:
#                     stack.append(int(num1/num2))
#         return stack[0]
