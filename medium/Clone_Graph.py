"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        def next_node(node, adj_node):
            for neighbor in node.neighbors:
                if neighbor in val_dict:
                    if val_dict[neighbor] in adj_node.neighbors:
                        break
                    adj_node.neighbors.append(val_dict[neighbor])
                else:
                    val_dict[neighbor] = Node(neighbor.val, [])
                    adj_node.neighbors.append(val_dict[neighbor])
                next_node(neighbor, adj_node.neighbors[-1])
        val_dict = {}
        ans = Node(node.val, [])
        val_dict[node] = ans
        next_node(node, ans)
        return ans
        
        
        
        
# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
# """

# class Solution:
#     def __init__(self):
#         self.visited = {}
        
#     def cloneGraph(self, node: 'Node') -> 'Node':
#         if not node:
#             return node     # None
#         if node in self.visited:
#             return self.visited[node]
        
#         clone = Node(node.val, [])
#         self.visited[node] = clone
        
#         if node.neighbors:
#             for n in node.neighbors:
#                 clone.neighbors.append(self.cloneGraph(n))
            
#         return clone
