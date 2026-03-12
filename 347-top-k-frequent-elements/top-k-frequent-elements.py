class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f={}
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        l=list(f.items())
        l.sort(key=lambda x:x[1],reverse=True)
        r=[]
        for i in range(k):
            r.append(l[i][0])
        return r
        