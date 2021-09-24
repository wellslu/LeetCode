# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        next_queue = []
        while True:
            for q in queue:
                if q.left is not None:
                    next_queue.append(q.left)
                if q.right is not None:
                    next_queue.append(q.right)
            if next_queue:
                queue = next_queue
                next_queue = []
            else:
                cnt = 0
                for q in queue:
                    cnt += q.val
                break
        return cnt
