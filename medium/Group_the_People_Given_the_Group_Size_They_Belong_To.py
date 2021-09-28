class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        target_dict = {}
        answer = []
        for index in range(len(groupSizes)):
            if groupSizes[index] in target_dict.keys():
                target_dict[groupSizes[index]].append(index)
            else:
                target_dict[groupSizes[index]] = [index]
            if len(target_dict[groupSizes[index]]) == groupSizes[index]:
                answer.append(target_dict[groupSizes[index]])
                target_dict[groupSizes[index]] = []
        return answer
