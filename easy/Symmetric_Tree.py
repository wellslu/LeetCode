# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        def next_node(left, right):
            if left is not None and right is not None and left.val == right.val:
                if left.left != right.right:
                    if not next_node(left.left, right.right):
                        return False
                
                if left.right != right.left:
                    if not next_node(left.right, right.left):
                        return False
                return True
            else:
                return False
        return next_node(root.left, root.right)
