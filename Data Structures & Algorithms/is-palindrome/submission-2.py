class Solution:
    def isPalindrome(self, s: str) -> bool:
        cmp0,cmp1='',''
        for i in range(len(s)):
            if s[i].isalnum():
                cmp0+=s[i].lower()
        for i in range(len(s)-1,-1,-1):
            if s[i].isalnum():
                cmp1+=s[i].lower()
        return(cmp0==cmp1)

        