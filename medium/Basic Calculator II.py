class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = []
        n = ''
        index = 0
        while index < len(s):
            if s[index] == '+':
                stack.append(int(n))
                n = ''
            elif s[index] == '-':
                stack.append(int(n))
                n = '-'
                while index+1 < len(s) and s[index+1].isdigit():
                    index+=1
                    n+=s[index]
            elif s[index] == '*':
                if n == '':
                    n = stack.pop()
                nn = ''
                while index+1 < len(s) and s[index+1].isdigit():
                    index+=1
                    nn+=s[index]
                n = int(n)*int(nn)
            elif s[index] == '/':
                if n == '':
                    n = stack.pop()
                nn = ''
                while index+1 < len(s) and s[index+1] in digits:
                    index+=1
                    nn+=s[index]
                n = int(n)/int(nn)
            else:
                n+=s[index]
            index+=1
        if n != '':
            stack.append(int(n))
        return sum(stack)
