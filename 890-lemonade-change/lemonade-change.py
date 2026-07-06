class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a=0
        b=0
        c=0
        for i in bills:
            if i==5:
                a+=1
            elif i==10:
                b+=1
                if a==0:
                    return False
                else:
                    a-=1
            elif i == 20:
                if b >= 1 and a >= 1:
                    b -= 1
                    a -= 1
                elif a >= 3:
                    a -= 3
                else:
                    return False
        return True