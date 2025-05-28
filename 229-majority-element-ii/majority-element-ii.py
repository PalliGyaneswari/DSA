class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l={}
        for i in nums:
            if i in l:
                l[i]+=1
            else:
                l[i]=1
        res=[]
        for i in l:
            if l[i]>len(nums)//3:
                res.append(i)
        return res

        