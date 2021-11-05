# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def next_node(self, root):
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [root.val]
        else:
            return self.next_node(root.left) + [root.val] + self.next_node(root.right)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        else:
            return self.next_node(root.left) + [root.val] + self.next_node(root.right)
