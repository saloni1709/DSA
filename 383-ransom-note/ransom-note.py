class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        f = {}
        f1 = {}

        for i in magazine:
            f[i] = f.get(i, 0) + 1
        for j in ransomNote:
            f1[j] = f1.get(j, 0) + 1
        
        for ch in f1:
            if ch not in f:
                return False
            if f[ch] < f1[ch]:
                return False
        return True
