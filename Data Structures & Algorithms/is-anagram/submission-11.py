class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (not t) or (not s):
            return False
        if len(s)!=len(t):
            return False
        countNum={}
        for si in s:
            if si not in countNum.keys():
                countNum[si]=s.count(si)
        for ti in t:
            if ti not in countNum.keys():
                return False
            if countNum[ti] != t.count(ti):
                return False
        return True

        