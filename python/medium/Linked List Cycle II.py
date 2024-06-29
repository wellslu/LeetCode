# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        node_list = [head]
        while head.next is not None:
            if head.next in node_list:
                return head.next
            head = head.next
            node_list.append(head)
        return None
      
      
      
      
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         if head is None:
#             return None
#         node_list = {head:1}
#         while head.next is not None:
#             if head.next in node_list:
#                 return head.next
#             head = head.next
#             node_list[head] = 1
#         return None
