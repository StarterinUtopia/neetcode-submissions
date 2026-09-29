class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=''
        for a in s:
            if a.isalnum():
                new+=a.lower()
        return new==new[::-1]
        