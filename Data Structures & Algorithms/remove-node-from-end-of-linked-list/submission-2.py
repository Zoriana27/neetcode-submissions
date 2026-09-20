# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        if not head.next:
            return None
        
        length = 0
        d = head
        while d and d.next:
            length += 1
            d = d.next
        length += 1
        if length - n == 0:
            return head.next
        dummy = head
        while i < length - n - 1:
            dummy = dummy.next
            i += 1
        
        dummy.next = dummy.next.next
        
        return head

        