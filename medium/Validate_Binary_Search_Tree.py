# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def next_node(node):
            val = node.val
            if node.right is None and node.left is None:
                return [node]
            else:
                if node.left is not None:
                    left_list = next_node(node.left)
                    if not left_list:
                        return False
                    for left_node in left_list:
                        if val <= left_node.val:
                            return False
                else:
                    left_list = []
                if node.right is not None:
                    right_list = next_node(node.right)
                    if not right_list:
                        return False
                    for right_node in right_list:
                        if val >= right_node.val:
                            return False
                else:
                    right_list = []
                return left_list + [node] + right_list
        if not next_node(root):
            return False
        else:
            return True
