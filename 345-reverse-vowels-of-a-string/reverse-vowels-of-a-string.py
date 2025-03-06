class Solution:
    def reverseVowels(self, s: str) -> str:
        v=['a','e','i','o','u','A','E','I','O','U']
        l=[]
        for i in s:
            if i in v:
                l.append(i)
        a=""
        for i in s:
            if i in v:
                a+=l.pop()
            else:
                a+=i
        return a
