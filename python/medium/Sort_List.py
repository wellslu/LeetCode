# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next
        nums.sort()
        new_head = ListNode(nums[0])
        node = new_head
        for num in nums[1:]:
            node.next = ListNode(num)
            node = node.next
        return new_head
