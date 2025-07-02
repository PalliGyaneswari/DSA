class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1=0
        p2=0
        l=[]
        maxi=0
        while p2<len(s):
            if s[p2] not in l:
                l.append(s[p2])
                p2+=1
                maxi=max(len(l),maxi)

            else:
                l.pop(0)
                p1+=1
    
        return maxi




        