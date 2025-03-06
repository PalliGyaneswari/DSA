class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p=s.split()
        s=p[len(p)-1]
        return len(s)