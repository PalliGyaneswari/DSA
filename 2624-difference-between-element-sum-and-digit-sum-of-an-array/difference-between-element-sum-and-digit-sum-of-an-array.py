class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s1=sum(nums)
        l=list(nums)
        s=''.join(map(str,l))
        s2=0
        for i in s:
            s2+=int(i)
        return abs(s1-s2)

        