class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        rev = ""

        for ch in s.lower():
            if ch.isalnum():
                rev = rev+ch
        
        if rev == rev[::-1]:
            return True
        else:
            return False
        

        