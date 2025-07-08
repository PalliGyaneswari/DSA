class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return 1
        else:
            ans=1
            c=1
            for i in range(1,len(nums)):
                if nums[i]-nums[i-1]==1:
                    c+=1
                    ans=max(ans,c)
                elif nums[i]==nums[i-1]:
                    continue
                else:
                    c=1
        return ans


        