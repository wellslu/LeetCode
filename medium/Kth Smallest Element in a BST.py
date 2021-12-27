# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node = root
        stack = []
        while True:
            while node.left is not None:
                stack.append(node)
                node = node.left
            k-=1
            if k == 0:
                return node.val
            while node.right is None:
                node = stack.pop()
                k-=1
                if k == 0:
                    return node.val
            node = node.right
