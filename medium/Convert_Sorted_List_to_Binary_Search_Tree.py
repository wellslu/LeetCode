# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        num_list = []
        while head.next != None:
            num_list.append(head.val)
            head = head.next
        num_list.append(head.val)
        def next_node(node, list_n):
            pivot = int(len(list_n)/2)
            pre = list_n[:pivot]
            back = list_n[pivot+1:]
            node.val = list_n[pivot]
            if len(pre) > 0:
                node.left = TreeNode()
                next_node(node.left, pre)
            if len(back) > 0:
                node.right = TreeNode()
                next_node(node.right, back)
        pivot = int(len(num_list)/2)
        pre = num_list[:pivot]
        back = num_list[pivot+1:]
        tree = TreeNode(num_list[pivot])
        if len(pre) > 0:
            tree.left = TreeNode()
            next_node(tree.left, pre)
        if len(back) > 0:
            tree.right = TreeNode()
            next_node(tree.right, back)
        return tree
