# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def make_tree(sort_list):
            tree = TreeNode(sort_list[0])
            for i in sort_list[1:]:
                node = tree
                while True:
                    if i > node.val:
                        if node.right is None:
                            node.right = TreeNode(i)
                            break
                        else:
                            node = node.right
                    if i < node.val:
                        if node.left is None:
                            node.left = TreeNode(i)
                            break
                        else:
                            node = node.left
            return tree
        def make_sort_list(n_list):
            sort_list = []
            if len(n_list) <= 1:
                return [n_list]
            for index in range(len(n_list)):
                for left_sort in make_sort_list(n_list[:index]):
                    for right_sort in make_sort_list(n_list[index+1:]):
                        sort_list.append([n_list[index]]+left_sort+right_sort)
            return sort_list
        sort_lists = make_sort_list([i for i in range(1, n+1)])
        ans = []
        for sort_list in sort_lists:
            ans.append(make_tree(sort_list))
        return ans
