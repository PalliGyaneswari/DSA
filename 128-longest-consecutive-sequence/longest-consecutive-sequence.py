class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        st=set(nums)
        l=1
        c=0
        for i in st:
            if i-1 not in st:
                c=1
                x=i
                while x+1 in st:
                    x+=1
                    c+=1
            l=max(l,c)
        return l

        