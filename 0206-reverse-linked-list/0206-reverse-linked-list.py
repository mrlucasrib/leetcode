# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        next_node = None
        new_list = None
        while curr is not None:
            next_node = curr.next
            curr.next = new_list
            new_list = curr
            curr = next_node
        return new_list
        