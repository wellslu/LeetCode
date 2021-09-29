# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @staticmethod
    def grandchildren_sum(node: TreeNode) -> int:
        grandnode_sum = 0
        if node.left is not None:
            if node.left.left is not None:
                grandnode_sum+=node.left.left.val
            if node.left.right is not None:
                grandnode_sum+=node.left.right.val
        if node.right is not None:
            if node.right.left is not None:
                grandnode_sum+=node.right.left.val
            if node.right.right is not None:
                grandnode_sum+=node.right.right.val
        return grandnode_sum
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        queue = [root]
        next_queue = []
        answer = 0
        while queue:
            for n in queue:
                if n.val % 2 == 0:
                    answer+=self.grandchildren_sum(n)
                if n.left is not None:
                    next_queue.append(n.left)
                if n.right is not None:
                    next_queue.append(n.right)
            queue = next_queue
            next_queue = []
        return answer
