class Solution:
    def constructRectangle(self,area):
        min=10000000
        for i in range(int(area**(1/2)),area+1):
            a=int(area/i)
            if area%i==0:
                if i>=a and i-a<min:
                    min=i-a
                    B=[i,a]
        return B