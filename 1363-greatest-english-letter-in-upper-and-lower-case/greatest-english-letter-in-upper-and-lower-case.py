class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        max = 0
        for i in s:
            if i.islower() and i.upper() in s:
                num = ord(i)
                if num > max:
                    max = num
            
        if max == 0:
            return ""
            
        return chr(max).upper()
