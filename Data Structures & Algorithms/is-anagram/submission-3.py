class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (not t) or (not s):
            return False
        if len(t)!=len(s):
            return False
        sSet=[]
        tSet=[]
        for i in range(0,len(s)):
            sSet.append(s[i])
            tSet.append(t[i])
        sSet.sort()
        tSet.sort()
        if  sSet!= tSet:
            return False
        return True