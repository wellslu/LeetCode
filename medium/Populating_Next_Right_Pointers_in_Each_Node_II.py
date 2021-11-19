"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = [root]
        while queue:
            new_queue = []
            for node in queue:
                if node.left is not None:
                    new_queue.append(node.left)
                if node.right is not None:
                    new_queue.append(node.right)
            if new_queue:
                for index in range(len(new_queue)-1):
                    new_queue[index].next = new_queue[index+1]
            queue = new_queue
        return root
