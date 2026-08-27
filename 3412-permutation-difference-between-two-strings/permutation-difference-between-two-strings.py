class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        total = 0
        for ch in s:
            i = s.index(ch)
            j = t.index(ch)

            total += abs(i - j)
        return total
