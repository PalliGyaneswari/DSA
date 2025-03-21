class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        l=0
        h=r*c-1
        while l<=h:
            m=(l+h)//2
            n=m//c
            m1=m%c
            if matrix[n][m1]==target:
                return True
            elif matrix[n][m1]<target:
                l=m+1
            else:
                h=m-1
        return False    
        