class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(list(set(nums)))
        longest_consecutive = 1
        consecutive = 1
        for index in range(1, len(nums)):
            if nums[index] == nums[index-1]+1:
                consecutive+=1
            else:
                if consecutive > longest_consecutive:
                    longest_consecutive = consecutive
                consecutive = 1
        if consecutive > longest_consecutive:
            longest_consecutive = consecutive
        return longest_consecutive
