# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        h=ListNode(0)
        h.next=head
        c=h
        while c.next:
            if c.next.val==val:
                c.next=c.next.next
            else:
                c=c.next
        return h.next
        