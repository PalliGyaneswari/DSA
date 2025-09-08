# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev,curr=None,slow
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        l,r=head,prev
        while r:
            if l.val!=r.val:
                return False
            l=l.next
            r=r.next
        return True
