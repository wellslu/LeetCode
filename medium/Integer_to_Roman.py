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
