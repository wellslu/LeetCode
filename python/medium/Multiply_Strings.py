class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        answer = 0
        for num1_index, num1_n in enumerate(num1[::-1]):
            num1_digit = int(num1_n+'0'*num1_index)
            for num2_index, num2_n in enumerate(num2[::-1]):
                num2_digit = int(num2_n+'0'*num2_index)
                answer+=(num1_digit*num2_digit)
        return str(answer)
