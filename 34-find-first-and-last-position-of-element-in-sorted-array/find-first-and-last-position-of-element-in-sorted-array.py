class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lb(nums,target):
            l=0
            h=len(nums)-1
            res=-1
            while l<=h:
                m=(l+h)//2
                if nums[m]==target:
                    res=m
                    h=m-1
                elif nums[m]<target:
                    l=m+1
                else:
                    h=m-1
            return res
        def hb(nums,target):
            l=0
            h=len(nums)-1
            res=-1
            while l<=h:
                m=(l+h)//2
                if nums[m]==target:
                    res=m
                    l=m+1
                elif nums[m]<target:
                    l=m+1
                else:
                    h=m-1
            return res

        return [lb(nums,target),hb(nums,target)]         