class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        d=0
        r=[]
        for i in s:
            if i=='(':
                if d>0:
                    r.append(i)
                d+=1
            elif i==')':
                d-=1
                if d>0:
                    r.append(i)
        return ''.join(r)
                
                


        