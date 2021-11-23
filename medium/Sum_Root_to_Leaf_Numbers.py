# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def next_node(node, num):
            if node.left is None and node.right is None:
                self.ans+=num*10+node.val
                return;
            num*=10
            if node.left is not None:
                next_node(node.left, num+node.val)
            if node.right is not None:
                next_node(node.right, num+node.val)
        next_node(root, 0)
        return self.ans
