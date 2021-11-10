# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        while True:
            move2front = head
            head_copy = head
            count_k = 0
            node = ListNode(head_copy.val)
            node_next = node
            while head_copy.next != None:
                if count_k == k:
                    move2front = move2front.next
                    node_next.next = ListNode(move2front.val)
                    node_next = node_next.next
                else:
                    count_k+=1
                head_copy = head_copy.next
            if k-count_k > 0:
                k=k%(count_k+1)
            else:
                break
        head_copy.next = node    
        return move2front.next
