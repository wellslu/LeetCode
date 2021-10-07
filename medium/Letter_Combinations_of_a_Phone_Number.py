class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        digits_dict = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        queue = []
        answer_len = 1
        for digit in digits:
            answer_len*=len(digits_dict[digit])
            queue.append(digits_dict[digit])
        answer = ['']*answer_len
        for en_str in queue:
            gap = len(en_str)
            for index, en in enumerate(en_str):
                while index < answer_len:
                    answer[index] = answer[index] + en
                    index+=gap
            answer.sort()
        return answer
