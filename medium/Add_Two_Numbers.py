# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_str = ''
        while l1.next is not None:
            l1_str = str(l1.val) + l1_str
            l1 = l1.next
        l1_str = str(l1.val) + l1_str
        
        l2_str = ''
        while l2.next is not None:
            l2_str = str(l2.val) + l2_str
            l2 = l2.next
        l2_str = str(l2.val) + l2_str
        
        l3_str = str(int(l1_str) + int(l2_str))
        l3 = ListNode(int(l3_str[0]))
        for i in l3_str[1:]:
            last_head_val = l3.val
            last_head_next=l3.next
            l3.val=i
            l3.next=ListNode()
            l3.next.val=last_head_val
            l3.next.next=last_head_next
        
        return l3
