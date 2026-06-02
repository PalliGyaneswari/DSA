class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r=[[1]]
        for i in range(1,numRows):
            prev=r[i-1]
            curr=[1]
            for j in range(len(prev)-1):
                curr.append(prev[j]+prev[j+1])
            curr.append(1)
            r.append(curr)
        return r
        
        