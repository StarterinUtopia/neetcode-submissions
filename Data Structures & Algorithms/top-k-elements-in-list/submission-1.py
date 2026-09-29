class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntDict = defaultdict()
        res = list()
        for num in nums:
            if num not in cntDict.keys():
                cntDict[num] = nums.count(num)
        for key,value in sorted(cntDict.items(),key = lambda x:(x[1],x[0]),reverse= True):
            if k>0:
                res.append(int(key))
                k-=1
        return res


        