# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        
        flag = False
        dummy = head
        while dummy:
            arr.append(dummy)
            dummy = dummy.next
        left, right = 1, len(arr) - 1
        while head and left <= right:
            if flag:
                head.next = arr[left]
                left += 1
                
                
            else:
                head.next = arr[right]
                right -= 1
                
            head = head.next
            flag = not flag
        if head:
            head.next = None
                

        


            
            

        