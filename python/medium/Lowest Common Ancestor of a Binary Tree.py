# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def next_node(self, node):
        left = None
        right = None
        if node.left is not None:
            left = self.next_node(node.left)
            if type(left) is not bool:
                return left
        if node.right is not None:
            right = self.next_node(node.right)
            if type(right) is not bool:
                return right
        if [left, right, node==self.q, node==self.p].count(True) == 2:
            return node
        elif [left, right, node==self.q, node==self.p].count(True) == 1:
            return True
        else:
            return False
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p, self.q = p, q
        return self.next_node(root)
