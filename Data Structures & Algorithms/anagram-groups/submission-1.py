class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not str:
            return[]
        pairs=sorted([("".join(sorted(s)),s) for s in strs])
        idx=0
        result=[[pairs[0][1]]]
        for i in range(1,len(strs)):
            if pairs[i][0]==pairs[i-1][0]:
                result[idx].append(pairs[i][1])
            else:
                idx+=1
                result.append([pairs[i][1]])
        return result    







