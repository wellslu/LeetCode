class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for i in nums_set:
            nums.remove(i)
        return list(nums_set.difference(set(nums)))[0]
      
      
      
      
      
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         return int((sum(set(nums))*3 - sum(nums))/2)
