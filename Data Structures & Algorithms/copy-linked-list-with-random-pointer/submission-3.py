"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        hm = {} # idx : ListNode
        curr = head

        while curr:
            hm[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            clone = hm[curr]
            clone.next = hm[curr.next] if curr.next else None
            clone.random = hm[curr.random] if curr.random else None

            curr = curr.next
        
        return hm[head]
        



