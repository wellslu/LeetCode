# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def next_node(self, p, q):
        if p is None or q is None or p.val != q.val:
            return False
        if p.left is not None or q.left is not None:
            if not self.next_node(p.left, q.left):
                return False
        if p.right is not None or q.right is not None:
            if not self.next_node(p.right, q.right):
                return False
        return True
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        return self.next_node(p, q)
