# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second = slow.next
        slow.next=None

        prev = None
        while second:
            next_=second.next
            second.next=prev
            prev=second
            second=next_
        
        second=prev
        dummy = head

        while second:
            temp2 = second.next
            second.next = head.next
            
            head.next = second
            head = second.next

            second=temp2
        


    

