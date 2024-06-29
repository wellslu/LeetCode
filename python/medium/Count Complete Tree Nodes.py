# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upper_node(self, h, node):
        node = node.right
        self.stack.append((h+1, node))
        return True, h+1, node
        
        
    def next_node(self, h, node):
        if node.left is not None and node.right is None:
            self.ans+=1
            self.h = max(self.h, h+1)
            self.stack = []
            return 0, 0, 0
        elif node.left is not None and node.right is not None:
            node = node.left
            self.stack.append((h+1, node))
            self.h = max(self.h, h+1)
            return True, h+1, node
        else:
            if h != self.h:
                self.stack = []
                return 0, 0, 0
            self.ans+=1
            self.stack.pop()
            h, node = self.stack.pop()
            return False, h, node
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.stack = [(0,0), (0, root)]
        self.h = 0
        self.ans = 0
        key = True
        h, node = 0, root
        while self.stack:
            if key:
                key, h, node = self.next_node(h, node)
            else:
                key, h, node = self.upper_node(h, node)
        for i in range(self.h):
            self.ans+=2**i
        return self.ans
