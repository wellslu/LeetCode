class Solution:
    def check_merge(self, answer: List[List[int]]) -> List[List[int]]:
        index = 0
        while len(answer) != index and index != len(answer)-1:
            if answer[index][1] >= answer[index+1][1]:
                if answer[index][0] <= answer[index+1][0]:
                    answer.pop(index+1)
                elif answer[index][0] > answer[index+1][1]:
                    t = answer[index]
                    answer[index] = answer[index+1]
                    answer[index+1] = t
                    index+=1
                else:
                    answer[index] = [answer[index+1][0], answer[index][1]]
            else:
                if answer[index][1] < answer[index+1][0]:
                    break
                elif answer[index][0] >= answer[index+1][0]:
                    answer.pop(index)
                else:
                    answer[index] = [answer[index][0], answer[index+1][1]]
        return answer

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = [intervals[0]]
        for interval in intervals[1:]:
            answer = [interval] + answer
            answer = self.check_merge(answer)
            print(answer)
        return answer
      
      
      
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         # O(nlogn)
        
#         # sort intervals, sort by first interval index
#         intervals.sort(key=lambda i:i[0])
        
#         # initialize with first interval
#         ans = [intervals[0]]

        
#         for first, second in intervals[1:]:
#             last_second = ans[-1][1]
       
#             if first <= last_second:
#                 ans[-1][1] = max(last_second, second)
#             else:
#                 ans.append([first, second])
        
#         return ans
