# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recursiveFindLeaf(self, node: TreeNode, target: TreeNode, route: List):
        if node.left is not None:
            if node.left == target:
                route.append(0)
                return route
            else:
                route_a = self.recursiveFindLeaf(node.left, target, route+[0])
                if route_a is None:
                    pass
                else:
                    return route_a
        if node.right is not None:
            if node.right == target:
                route.append(1)
                return route
            else:
                route_a = self.recursiveFindLeaf(node.right, target, route+[1])
                if route_a is None:
                    pass
                else:
                    return route_a
        
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target:
            return cloned
        else:
            route = self.recursiveFindLeaf(original, target, [])
            for r in route:
                if r == 0:
                    cloned = cloned.left
                else:
                    cloned = cloned.right
            return cloned
