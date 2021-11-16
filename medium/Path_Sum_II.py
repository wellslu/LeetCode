# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def next_node(node, num_list, sum_num):
            num_list = num_list + [node.val]
            sum_num = sum_num + node.val
            if node.left is None and node.right is None:
                if sum_num == targetSum:
                    ans.append(num_list)
            else:
                if node.left is not None:
                    next_node(node.left, num_list, sum_num)
                if node.right is not None:
                    next_node(node.right, num_list, sum_num)
        next_node(root, [], 0)
        return ans
