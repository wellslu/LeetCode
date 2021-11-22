class Solution:
    def __init__(self):
        self.minimum = None
        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        queue = {0:triangle[0][0]}
        for t in triangle[1:]:
            new_queue = {}
            for index in range(len(t)):
                new_queue[index] = []
                if index - 1 >= 0:
                    new_queue[index].append(queue[index-1]+t[index])
                if index < len(queue):
                    new_queue[index].append(queue[index]+t[index])
                new_queue[index] = min(new_queue[index])
            queue = new_queue
        return min(queue.values())
