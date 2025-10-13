class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        maxi=0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if i==j or i+j==len(nums)-1:
                    num=nums[i][j]
                    if num>1:
                        ip=True
                        for k in range(2,int(num**0.5)+1):
                            
                            if num%k==0:
                                ip=False
                                break
                        if ip:
                            maxi=max(num,maxi)
        return maxi
            