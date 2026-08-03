class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s)):
            curr = value[s[i]]
            if i < len(s) - 1:
                nxt = value[s[i+1]]

                if curr < nxt:
                    total -= curr
                else:
                    total += curr
            
            else:
                total += curr
        
        return total
        
        
        