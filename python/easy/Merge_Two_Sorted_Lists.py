# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            ans = ListNode(l2.val)
            l2 = l2.next
        elif l2 is None:
            ans = ListNode(l1.val)
            l1 = l1.next
        elif l1.val <= l2.val:
            ans = ListNode(l1.val)
            l1 = l1.next
        else:
            ans = ListNode(l2.val)
            l2 = l2.next
        while l1 is not None and l2 is not None:
            j = ans
            while j.next is not None:
                j = j.next
            if l1.val <= l2.val:
                j.next = ListNode(l1.val)
                l1 = l1.next
            else:
                j.next = ListNode(l2.val)
                l2 = l2.next
        if l2 is not None:
            while l2 is not None:
                j = ans
                while j.next is not None:
                    j = j.next
                j.next = ListNode(l2.val)
                l2 = l2.next
        if l1 is not None:
            while l1 is not None:
                j = ans
                while j.next is not None:
                    j = j.next
                j.next = ListNode(l1.val)
                l1 = l1.next
        return ans
