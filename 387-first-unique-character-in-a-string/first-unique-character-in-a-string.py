class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        fre = {}

        for ch in s:
            fre[ch] = fre.get(ch, 0) + 1
        for idx, val in enumerate(s):
            if fre[val] == 1:
                return idx
                break
        return -1

        
