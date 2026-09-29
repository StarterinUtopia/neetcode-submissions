class Solution:
    def trap(self, height: List[int]) -> int:
        L,R=0,len(height)-1
        lmax,rmax=0,0
        res=0
        while L<R:
            if height[L]<height[R]:
                if height[L]>lmax:
                    lmax=height[L]
                else:
                    res+=lmax-height[L]
                L+=1
            else:
                if height[R]>rmax:
                    rmax=height[R]
                else:
                    res+=rmax-height[R]
                R-=1
        return res