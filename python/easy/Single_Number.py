class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        queue = []
        for i in nums:
            if i in queue:
                queue.remove(i)
            else:
                queue.append(i)
        return queue[0]
      
      
      
      
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         return 2*sum(set(nums))-sum(nums)




# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         for elem in nums[1:]:
#             nums[0] = nums[0] ^ elem
#         return nums[0]
