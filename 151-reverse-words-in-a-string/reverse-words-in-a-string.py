class Solution:
    def reverseWords(self, s: str) -> str:
        l=[]
        c=0
        for i in range(len(s)+1):
            if  i==len(s) or s[i]==" ":
                l.append(s[c:i])
                c=i+1
        while "" in l:
            l.remove("")

        return ' '.join(l[::-1])
        