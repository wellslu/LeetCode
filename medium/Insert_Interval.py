class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        for index in range(len(intervals)):
            if intervals[index][1] >= newInterval[0]:
                if intervals[index][0] > newInterval[1]:
                    intervals.insert(index, newInterval)
                    break
                newInterval_list = [min(intervals[index][0], newInterval[0]), max(intervals[index][1], newInterval[1])]
                index_end = index+1
                while index_end < len(intervals) and intervals[index_end][0] <= newInterval[1]:
                    newInterval_list[1] = max(intervals[index_end][1], newInterval_list[1])
                    index_end+=1
                intervals = intervals[:index] + [newInterval_list] + intervals[index_end:]
                break
            if index == len(intervals)-1:
                intervals.append(newInterval)
        return intervals
      
