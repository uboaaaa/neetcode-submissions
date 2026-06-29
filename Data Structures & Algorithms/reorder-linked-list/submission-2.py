# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        mid = fast = head
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
        
        # reverse second half; mid is now pointing at mid-point
        prev, curr = None, mid.next
        mid.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # mesh reversed second-half with first half
        p1, p2 = head, prev
        while p2:
            t1 = p1.next
            t2 = p2.next
            p1.next = p2
            p1 = t1
            p2.next = p1
            p2 = t2
        
        
            


