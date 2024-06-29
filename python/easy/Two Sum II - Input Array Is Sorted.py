class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = len(numbers) - 1
        while first != second:
            if numbers[first] + numbers[second] == target:
                return [first+1, second+1]
            elif numbers[first] + numbers[second] > target:
                second-=1
            else:
                first+=1
