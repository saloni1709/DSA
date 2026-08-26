class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        word = set(s)
        max = 0
        for i in s:
            if i.islower() and i.upper() in word:
                if ord(i) > max:
                    max = ord(i)
        if max == 0:
            return ""
        return chr(max).upper()