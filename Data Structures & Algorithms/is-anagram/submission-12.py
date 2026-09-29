class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (not t) or (not s):
            return False
        if len(s)!=len(t):
            return False
        seen=[]
        for i in range(0,len(s)) :
            if s[i] not in seen:
                seen.append(s[i])
                if s[i] not in t:
                    return False
                if s.count(s[i]) != t.count(s[i]):
                    return False
        return True

        