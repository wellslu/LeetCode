class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        nums = sorted(nums)
        nums_set = set(nums)
        for i in nums_set:
            for j in set(nums[nums.index(i)+1:]):
                if i == j:
                    f = nums.index(j)+2
                else:
                    f = nums.index(j)+1
                s = len(nums) - 1
                while s > f:
                    distance = target - i - j - nums[f] - nums[s]
                    if distance == 0:
                        answer.append([i, j, nums[f], nums[s]])
                        num_f = nums[f]
                        num_s = nums[s]
                        s-=1
                        f+=1
                        while s > f and nums[f] == num_f:
                            f+=1
                        while s > f and nums[s] == num_s:
                            s-=1
                    elif distance > 0:
                        f+=1
                    else:
                        s-=1
        return answer
