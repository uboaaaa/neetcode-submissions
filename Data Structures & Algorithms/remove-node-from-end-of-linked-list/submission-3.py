# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # extract listnode length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        to_traverse = length - n
        dummy = ListNode(None, head)
        prev, curr = dummy, head

        while curr: 
            if to_traverse == 0:
                prev.next = prev.next.next
                break
            to_traverse -= 1
            curr = curr.next
            prev = prev.next
        
        return dummy.next

