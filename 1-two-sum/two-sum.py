class Solution(object):
    def twoSum(self, nums, target):
        h={}
        for i in range(len(nums)):
            c=target-nums[i]
            if c in h:
                return [h[c],i]
                break
            h[nums[i]]=i