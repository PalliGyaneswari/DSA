class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        l=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            p1=i+1
            p2=len(nums)-1
            while p1<p2:
                if nums[p1]+nums[p2]+nums[i]==0:
                    l.append([nums[p1],nums[p2],nums[i]])
                    while p1 < p2 and nums[p1] == nums[p1 + 1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2 - 1]:
                        p2 -= 1
                    p1+=1
                    p2-=1
                elif nums[p1]+nums[p2]+nums[i]<0:
                    p1+=1
                else:
                    p2-=1
        return l


        