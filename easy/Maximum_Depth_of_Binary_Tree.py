# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.depth = 0
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def next_node(node, d):
            self.depth = max(self.depth, d)
            if node.left is not None:
                next_node(node.left, d+1)
            if node.right is not None:
                next_node(node.right, d+1)
        next_node(root, 1)
        return self.depth
