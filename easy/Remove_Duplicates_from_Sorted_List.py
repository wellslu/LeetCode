# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        linked_list = head
        while linked_list.next is not None:
            if linked_list.val == linked_list.next.val:
                linked_list.next = linked_list.next.next
            else:
                linked_list = linked_list.next
        return head
