class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''.join(map(str,digits))
        s1=int(s)+1
        l=[]
        for i in str(s1):
            l.append(int(i))
        return l