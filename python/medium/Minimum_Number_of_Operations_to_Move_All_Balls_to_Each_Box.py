class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        for i in range(len(boxes)):
            cnt = 0
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    cnt += abs(i-j)
            answer.append(cnt)
        return answer
