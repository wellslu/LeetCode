# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        node_list = [head]
        while head.next is not None:
            if head.next in node_list:
                return True
            head = head.next
            node_list.append(head)
        return False
      
      
      
      
      
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         fast = slow = head
#         while fast and fast.next:
#             fast, slow = fast.next.next, slow.next
#             if slow is fast:
#                 return True
#         return False
