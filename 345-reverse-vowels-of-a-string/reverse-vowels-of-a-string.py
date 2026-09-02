class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s1 = list(s)
        l = 0
        r = len(s1) - 1
        vowels = 'aeiouAEIOU'
        while l < r:
            if s1[l] not in vowels:
                l += 1
            elif s1[r] not in vowels:
                r -= 1
            else:
                s1[l], s1[r] = s1[r], s1[l]
                l += 1
                r -= 1
        return "".join(s1)