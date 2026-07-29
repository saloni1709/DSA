class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        words = s.split()
        s = words[::-1]
        s = " ".join(s)

        return s