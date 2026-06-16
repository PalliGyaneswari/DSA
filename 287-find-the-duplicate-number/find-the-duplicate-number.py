class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h={}
        for i in nums:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        for v,c in h.items():
            if c==1:
                continue
            return v