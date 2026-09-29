class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs=sorted([("".join(sorted(s)),s) for s in strs])
        idx=0
        seen=set()
        seen.add(pairs[0][0])
        result=[[pairs[0][1]]]
        for i in range(1,len(strs)):
            word=pairs[i][0]
            if word in seen:
                result[idx].append(pairs[i][1])
            else:
                idx+=1
                result.append([pairs[i][1]])
                seen.add(pairs[i][0])
        return result    







