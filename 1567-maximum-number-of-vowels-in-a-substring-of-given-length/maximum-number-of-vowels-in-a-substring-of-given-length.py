class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        v = 'aeiou'
        count = 0

        for i in range(k):
            if s[i] in v:
                count += 1
        
        max_count = count

        for j in range(k, len(s)):
            if s[j-k] in v:
                count -= 1
            
            if s[j] in v:
                count += 1

            if count > max_count:
                max_count = count
            
        return max_count