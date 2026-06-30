# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0 :
            return head
        tail=head
        c=1
        while tail.next:
            c+=1
            tail=tail.next
            
        
        k=k%c
        if k==0:
            return head
        tail.next=head
        ro=c-k
        nhead=head
        for i in range(ro-1):
            nhead=nhead.next
        n_one=nhead.next
        nhead.next=None
        return n_one
            

        