class Solution:
    def firstUniqChar(self, s: str) -> int:
        f={}
        for i in s:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        for i in range(len(s)):
            if f[s[i]]==1:
                return i
        return -1            

        
        