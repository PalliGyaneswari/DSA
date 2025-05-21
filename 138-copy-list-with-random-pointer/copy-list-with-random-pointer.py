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
        o={}
        c=head
        while c:
            o[c]=Node(c.val)
            c=c.next
        c=head
        while c:
            o[c].next=o.get(c.next)
            o[c].random=o.get(c.random)
            c=c.next
        return o[head]
        