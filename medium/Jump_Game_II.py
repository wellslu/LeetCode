class Solution:
    # def next_jump(self, nums: List[int], step: int) -> int:
    #     if nums[0] >= len(nums)-1:
    #         return step+1
    #     max_index = 1
    #     for index in range(nums[0]-1):
    #         if nums[max_index]-(index+2)+max_index < nums[index+2]:
    #             max_index = index+2
    #     return self.next_jump(nums[max_index:], step+1)
    
    def jump(self, nums: List[int]) -> int:
        step = 0
        if len(nums)-1 == 0:
            return 0
        while nums[0] < len(nums)-1:
            max_index = 1
            for index in range(nums[0]-1):
                if nums[max_index]-(index+2)+max_index < nums[index+2]:
                    max_index = index+2
            nums = nums[max_index:]
            step+=1
        return step+1
      
#     def jump(self, nums: List[int]) -> int:
#         end = 0
#         maxPos = 0
#         step = 0
#         #if nums = None or nums[0] == 0:
#         #    return 0

#         for i in range(0,len(nums)-1):
#             maxPos = max(i+nums[i], maxPos)
#             if (i==end) :
#                 end = maxPos
#                 step+=1
#         return step
