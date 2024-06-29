# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans_node = ListNode(head.val)
        node = ans_node
        head = head.next
        while head is not None:
            val = head.val
            if val < node.val:
                ans_node = ListNode(val)
                ans_node.next = node
            else:
                while node.next is not None and node.next.val < val:
                    node = node.next
                j = node.next
                node.next = ListNode(val)
                node.next.next = j
            node = ans_node
            head = head.next
        return ans_node
