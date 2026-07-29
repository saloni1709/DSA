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

        # count = 0
        # for i in range(len(s)):
        #     count = s.count(s[i])

        #     if count == 1:
        #         return i

        # return -1
        
