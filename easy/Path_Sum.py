# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def next_node(node, sum_num):
            if node.left is None and node.right is None:
                if sum_num+node.val == targetSum:
                    return True
                else:
                    return False
            if node.left is not None:
                if next_node(node.left, sum_num+node.val):
                    return True
            if node.right is not None:
                if next_node(node.right, sum_num+node.val):
                    return True
            return False
        return next_node(root, 0)
