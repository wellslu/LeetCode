# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        index = 0
        if head.next != None:
            node1 = head
            head = head.next
            node1.next = head.next
            head.next = node1
        node = head.next
        while node != None and node.next != None and node.next.next != None:
            node1 = node.next
            node.next = node.next.next
            node1.next = node.next.next
            node.next.next = node1
            node = node.next.next
        return head
