class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        a=[True]*(n)
        a[0]=a[1]=False
        for i in range(2,int(n**0.5)+1):
            if a[i]:
                for i in range(i*i,n,i):
                    a[i]=False
        return sum(a)

