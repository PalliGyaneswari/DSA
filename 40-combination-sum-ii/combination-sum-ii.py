class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def sumi(i,path,ans,s):
            
            if s==target:
                if path[:] in ans:
                    return
                ans.append(path[:])
                return
            if i==len(candidates) or s>target:
                return

            path.append(candidates[i])
            sumi(i+1,path,ans,s+candidates[i])
            path.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            sumi(i+1,path,ans,s)
        ans=[]
        candidates.sort()
        sumi(0,[],ans,0)

        return ans
        