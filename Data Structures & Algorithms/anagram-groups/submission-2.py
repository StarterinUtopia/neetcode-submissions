class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sSort = "".join(sorted(s))
            res[sSort].append(s)
        return list(res.values())