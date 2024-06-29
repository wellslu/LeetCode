class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sort_number(queue):
            n = queue[0]
            if len(queue) == 1:
                return n
            for q in queue[1:]:
                if n+q < q+n:
                    n = q
            queue.remove(n)
            return n + sort_number(queue)
        nums = [str(num) for num in nums]
        ans = ''
        for i in range(9, -1, -1):
            i_list = list(filter(lambda x: x[0] == str(i), nums))
            if i_list:
                ans+=sort_number(i_list)
        return str(int(ans))
