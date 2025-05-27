class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l=[]
        l1=[]
        for i in nums:
            if i<0:
                l1.append(i)
            else:
                l.append(i)
        
        res=[]
        for i in range(len(l)):
            res.append(l[i])
            res.append(l1[i])
        return res