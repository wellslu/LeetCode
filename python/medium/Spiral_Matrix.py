class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        width = len(matrix[0])
        length = len(matrix)
        answer = []
        for r in range(int(min(width, length)/2+0.5)):
            x = r
            y = r
            answer.append(matrix[y][x])
            for w in range(1, width-2*r):
                x+=1
                answer.append(matrix[y][x])
            for l in range(1, length-2*r):
                y+=1
                answer.append(matrix[y][x])
            if length-2*r != 1:
                for w in range(1, width-2*r):
                    x-=1
                    answer.append(matrix[y][x])
            if width-2*r != 1:
                for l in range(1, length-2*r-1):
                    y-=1
                    answer.append(matrix[y][x])
        return answer
