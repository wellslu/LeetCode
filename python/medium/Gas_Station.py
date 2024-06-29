class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diffs = [gas[i]-cost[i] for i in range(len(gas))]
        index = 0
        if sum(diffs) < 0:
            return -1
        queue = []
        nums = 0
        for i, diff in enumerate(diffs):
            nums+=diff
            if nums < 0:
                index = i+1
                queue.append(nums)
                nums = 0
        queue.append(nums)
        if sum(queue) >= 0:
            return index
        else:
            return -1
