class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for num in set(nums):
            f = nums.index(num)+1
            s = len(nums) - 1
            while s > f:
                result = num + nums[f] + nums[s]
                if result == 0:
                    answer.append([num, nums[f], nums[s]])
                    num_f = nums[f]
                    num_s = nums[s]
                    s-=1
                    f+=1
                    while s > f and nums[f] == num_f:
                        f+=1
                    while s > f and nums[s] == num_s:
                        s-=1
                elif result > 0:
                    s-=1
                else:
                    f+=1
        return answer
