class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                queue.append(i)
            else:
                if not queue:
                    return False
                elif queue[-1] == '(' and i == ')':
                    queue.pop()
                elif queue[-1] == '[' and i == ']':
                    queue.pop()
                elif queue[-1] == '{' and i == '}':
                    queue.pop()
                else:
                    return False
        if queue:
            return False
        else:
            return True
