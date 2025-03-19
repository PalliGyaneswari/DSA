class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        c=0
        p=0
        for i in reversed(columnTitle):
            d=ord(i)-64
            c+=d*26**p
            p+=1
        return c

        