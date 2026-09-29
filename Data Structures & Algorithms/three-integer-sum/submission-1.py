class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=nums[i]
            m=i+1
            n=len(nums)-1
            while m<n:
                currentSum=nums[m]+nums[n]+target
                if currentSum==0:
                    res.append([target,nums[m],nums[n]])
                    m+=1
                    n-=1
                    while m<n and nums[m]==nums[m-1]:
                        m+=1
                elif currentSum>0:
                    n-=1
                else:
                    m+=1
        return res