# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curr=head
        c=0
        while curr:
            c+=1
            curr=curr.next
        s=(c//2)+1
        sizz=head
        c1=0
        while sizz:
            c1+=1
            if c1==s:
                break
            sizz=sizz.next
        return sizz
        
        