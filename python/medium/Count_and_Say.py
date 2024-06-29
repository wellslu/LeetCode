class Solution:
    def countAndSay(self, n: int) -> str:
        answer = '1'
        for r in range(2, n+1):
            new_answer = ''
            c = answer[0]
            for w in answer[1:]:
                if w == c[0]:
                    # print(c, w)
                    c+=w
                else:
                    new_answer+=f'{len(c)}{c[0]}'
                    c=w
            answer = new_answer + f'{len(c)}{c[0]}'
        return answer
