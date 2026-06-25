# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        curr=head
        c=0
        while curr:
            c+=1
            curr=curr.next
        val=(c-n+1)

        if val == 1:
            return head.next



        sizz=head
        c1=0
        while sizz:
            c1+=1
            if c1==val-1:
                sizz.next=sizz.next.next
                break
            sizz=sizz.next
        return head
        

        