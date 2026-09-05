# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        def merge(first, second):
            dummy = ListNode(0)
            temp = dummy
            while first and second:
                if first.val < second.val:
                    temp.next = first
                    first = first.next
                else:
                    temp.next = second
                    second = second.next
                temp=temp.next
            temp.next = first if first else second
            return dummy.next

        while len(lists) > 1:
            merged = list()
            for i in range(0,len(lists),2):
                first = lists[i]
                second = lists[i+1] if i+1<len(lists) else None
                merged.append(merge(first,second))
            lists=merged
        return lists[0]
            
        
        
