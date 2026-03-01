class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_a=0
        while l<r:
            w=r-l
            h=min(height[l],height[r])
            a=w*h
            max_a=max(max_a,a)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_a        