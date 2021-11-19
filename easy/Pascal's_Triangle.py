class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for row in range(1, numRows):
            ans.append([])
            for i in range(row+1):
                if i == 0 or i == row:
                    ans[-1].append(1)
                else:
                    ans[-1].append(ans[-2][i-1]+ans[-2][i])
        return ans
