class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res,cnt=1,1
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if (nums[i]==nums[i-1]+1):
                cnt+=1                    
            elif (nums[i]==nums[i-1]):
                continue
            else:
                if cnt>res:
                    res=cnt
                cnt=1
        return max(res,cnt)




        