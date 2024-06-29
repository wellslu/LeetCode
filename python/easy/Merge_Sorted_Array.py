class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1.pop()
        i = 0
        for num in nums2:
            while i < len(nums1) and num > nums1[i]:
                i+=1
            nums1.insert(i, num)
        return nums1
