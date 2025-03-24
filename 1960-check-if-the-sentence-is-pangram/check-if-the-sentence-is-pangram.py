class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l=[]
        for i in sentence:
            if i in l:
                continue
            else:
                l.append(i)
        if len(l)==26:
            return True
        else:
            return False
        