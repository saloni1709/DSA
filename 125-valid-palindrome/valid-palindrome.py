class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        ans = ""
        for ch in s:
            if ch.isalnum():
                ans+=ch.lower()
            
        if ans == ans[::-1]:
            return True
        return False
