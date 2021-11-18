# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def next_node(node):
            if node.left is None and node.right is None:
                return 1
            if node.left is not None:
                left_d = next_node(node.left)
                if not left_d:
                    return False
            else:left_d=0
            if node.right is not None:
                right_d = next_node(node.right)
                if not right_d:
                    return False
            else:right_d=0
            if abs(right_d-left_d) > 1:
                return False
            return max(left_d, right_d) + 1
        if not next_node(root):
            return False
        return True
