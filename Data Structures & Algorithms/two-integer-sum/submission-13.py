class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs=[(val,idx) for idx,val in enumerate(nums)]
        pairs.sort()
        i,j=0,len(nums)-1
        while (i<j):
            if pairs[i][0]+pairs[j][0]==target:
                idx1,idx2=pairs[i][1],pairs[j][1]        
                return[min(idx1,idx2),max(idx1,idx2)]
            elif pairs[i][0]+pairs[j][0]>target:
                j-=1
            else:
                i+=1
            
                        

    