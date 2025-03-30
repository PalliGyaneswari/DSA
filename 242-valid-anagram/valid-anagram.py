class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f={}
        for i in s:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        f1={}
        for i in t:
            if i in f1:
                f1[i]+=1
            else:
                f1[i]=1
        if f==f1:
            return True
        else:
            return False