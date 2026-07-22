class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        f = {}
        f1 = {}

        for i in s:
            f[i] = f.get(i, 0) + 1
        for j in t:
            f1[j] = f1.get(j, 0) + 1

        if f == f1:
            return True
        else:
            return False        