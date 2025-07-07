class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1={}
        for i in s:
            if i in s1:
                s1[i]+=1
            else:
                s1[i]=1
        t1={}
        for i in t:
            if i in t1:
                t1[i]+=1
            else:
                t1[i]=1
        if len(set(zip(s, t))) == len(set(s)) == len(set(t)):
            return True
        else:
            return False
        