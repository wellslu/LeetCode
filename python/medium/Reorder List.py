# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None or head.next.next is None:
            return head
        node_dict = {}
        node = head
        i = 0
        while node is not None:
            node_dict[i] = node
            i+=1
            node = node.next
        
        length = len(node_dict)
        node = head
        i = 0
        for i in range(1, int(len(node_dict)/2)):
            node.next = node_dict[length-i]
            node = node.next
            node.next = node_dict[i]
            node = node.next
        i+=1
        node.next = node_dict[length-i]
        node = node.next
        if length % 2 == 1:
            node.next = node_dict[i]
            node = node.next
        node.next = None
        return head
        
