class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f = 0
        s = len(nums) - 1
        if nums[f] == target:
                return f
        elif nums[s] == target:
                return s
        while f <= s:
            m = int((s-f)/2) + f
            if nums[m] == target:
                return m
            elif nums[f]<=nums[m]:
                if nums[f]<=target<nums[m]:
                    s = m - 1
                else:
                    f = m + 1
            else:
                if nums[s]>=target>nums[m]:
                    f = m + 1
                else:
                    s = m - 1
        else:
            return -1
