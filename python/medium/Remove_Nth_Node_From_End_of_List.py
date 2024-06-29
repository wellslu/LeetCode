# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current_node = head
        last_nnode = head
        next_nnode = head
        if next_nnode.next == None:
            return None
        for r in range(n-1):
            if next_nnode.next != None:
                last_nnode = next_nnode
                next_nnode = next_nnode.next
            else:
                last_nnode.next = None
                return head
        last_nnode = head
        while next_nnode.next != None:
            last_nnode = current_node
            next_nnode = next_nnode.next
            current_node = current_node.next
        if current_node == last_nnode:
            return head.next
        else:
            last_nnode.next = last_nnode.next.next
            return head
