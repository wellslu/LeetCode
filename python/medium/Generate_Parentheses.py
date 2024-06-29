class Solution:
    def __init__(self):
        self.answer = []
    
    def next_parentheses(self, answer, n):
        if answer.count('(') == n and answer.count(')') == n-1:
            self.answer.append(answer+')')
            return;
        if answer.count('(') < n:
            self.next_parentheses(answer+'(', n)
        if answer.count('(') > answer.count(')'):
            self.next_parentheses(answer+')', n)
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.next_parentheses('(', n)
        return self.answer
