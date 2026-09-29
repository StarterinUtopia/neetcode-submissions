class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        le=len(heights)
        for i in range(le-1):
            for j in range(i,le):
                storage= (j-i)*min(heights[i],heights[j])
                if storage>max:
                    max=storage
        return max
            
    
        