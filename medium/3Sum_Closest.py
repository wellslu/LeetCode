class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        answer = sum(nums[:3])
        gap = abs(target - answer)
        for num in set(nums):
            index = nums.index(num)
            f = index+1
            s = len(nums)-1
            while s > f and gap != 0:
                num_f = nums[f]
                num_s = nums[s]
                answer_t = num + num_f + num_s
                gap_t = target - answer_t
                if abs(gap_t) < gap:
                    gap = abs(gap_t)
                    answer = answer_t
                f+=1
                s-=1
                while s > f and nums[f] == num_f:
                    f+=1
                while s > f and nums[s] == num_s:
                    s-=1
                if gap_t > 0:
                    s+=1
                else:
                    f-=1
        return answer
