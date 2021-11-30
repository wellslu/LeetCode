class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        def maxProduct_part(nums_part):
            if not nums_part:
                return 0
            if len(nums_part) == 1:
                return nums_part[0]
            num_sum = 1
            for num in nums_part:
                num_sum*=num
            if num_sum > 0:
                return num_sum
            n1 = 1
            n2 = 1
            for num in nums_part:
                n1*=num
                if num < 0:
                    break
            for num in nums_part[::-1]:
                n2*=num
                if num < 0:
                    break
            if n2 > n1:
                return num_sum/n2
            else:
                return num_sum/n1
        start = 0
        for index in range(len(nums)):
            if nums[index] == 0:
                product = maxProduct_part(nums[start:index])
                if product > ans:
                    ans = product
                start = index+1
        product = maxProduct_part(nums[start:])
        if product > ans:
            ans = product
        if ans < 0 and 0 in nums:
            return 0
        else:
            return int(ans)
