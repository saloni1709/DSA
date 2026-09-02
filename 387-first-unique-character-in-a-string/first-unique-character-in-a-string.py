class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        f = {}
        for i in s:
            f[i] = f.get(i, 0) + 1
        
        for idx, val in enumerate(s):
            if f[val] == 1:
                return idx
        return -1