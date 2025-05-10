# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer1, pointer2 = head, head
        for _ in range(n):
            pointer2 = pointer2.next
        if not pointer2:
            return head.next
        
        while pointer2.next is not None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        
        
        pointer1.next = pointer1.next.next

        return head