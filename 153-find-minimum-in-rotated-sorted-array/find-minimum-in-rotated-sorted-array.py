class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l=0
        h=len(nums)-1
        while l<=h:
            m=(l+h)//2
            p=(m+1)%len(nums)
            n=(m-1+len(nums))%len(nums)
            if nums[m]<nums[p] and nums[m]<nums[n]:
                return nums[m]
            elif nums[m]>nums[h]:
                l=m+1
            else:
                h=m-1
        