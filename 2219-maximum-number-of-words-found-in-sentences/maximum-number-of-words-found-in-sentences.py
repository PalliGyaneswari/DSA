class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m=0
        for i in sentences:
            w=len(i.split())
            m=max(m,w)
        return m

        