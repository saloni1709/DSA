class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # rev = ""

        # for ch in s.lower():
        #     if ch.isalnum():
        #         rev = rev+ch
        
        # if rev == rev[::-1]:
        #     return True
        # else:
        #     return False
        
        l = 0
        r = len(s) - 1

        while l < r:

            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True
        