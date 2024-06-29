# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = [[]]
        def next_node(node, layer):
            if len(ans) < layer:
                ans.append([])
            ans[layer-1].append(node.val)
            if node.left is not None:
                next_node(node.left, layer+1)
            if node.right is not None:
                next_node(node.right, layer+1)
        next_node(root, 1)
        return ans
