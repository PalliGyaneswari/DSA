class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        c=0
        i=1
        v=False
        while(1):
            if i not in arr:
                c+=1
                if c==k:
                    return i
              

            i+=1
        
