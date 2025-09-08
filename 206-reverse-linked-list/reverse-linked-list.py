# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=None
        curr=head
        while curr:
            n=curr.next
            curr.next=p
            p=curr
            curr=n
        return p
        