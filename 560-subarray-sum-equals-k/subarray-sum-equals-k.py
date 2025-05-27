class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s=0
        c=0
        map={0:1}
        for i in nums:
            s+=i
            if s-k in map:
                c+=map[s-k]
            if s in map:
                map[s]+=1
            else:
                map[s]=1
        return c