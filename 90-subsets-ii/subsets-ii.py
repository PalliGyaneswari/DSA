class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def sub(i,path,ans):
            if i==len(nums):
                if path[:] in ans:
                    return
                ans.append(path[:])
                return
            
            path.append(nums[i])
            sub(i+1,path,ans)
            path.pop()
            sub(i+1,path,ans)
        ans=[]
        nums.sort()
        sub(0,[],ans)
        return ans
        