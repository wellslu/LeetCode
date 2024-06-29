# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.layer_dict = {}
    
    def next_node(self, node, layer):
        if node is None:
            return ;
        if layer in self.layer_dict:
            self.layer_dict[layer].append(node.val)
        else:
            self.layer_dict[layer] = [node.val]
        self.next_node(node.left, layer+1)
        self.next_node(node.right, layer+1)
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None
        self.layer_dict[0] = [root.val]
        self.next_node(root.left, 1)
        self.next_node(root.right, 1)
        ans = []
        for i in self.layer_dict:
            ans.append(self.layer_dict[i][-1])
        return ans
