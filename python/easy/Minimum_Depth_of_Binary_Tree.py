# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.min_depth = None
        
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def next_node(node, depth):
            if node.left is None and node.right is None:
                if self.min_depth is None or depth < self.min_depth:
                    self.min_depth = depth
                    return;
            elif self.min_depth is not None and depth >= self.min_depth:
                return;
            if node.left is not None:
                next_node(node.left, depth+1)
            if node.right is not None:
                next_node(node.right, depth+1)
        next_node(root, 1)
        return self.min_depth
