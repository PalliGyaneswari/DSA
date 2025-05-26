class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        min=float('inf')
        for i in prices:
            if i<min:
                min=i
            else:
                p=i-min
                maxi=max(p,maxi)
        return maxi

        