class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        window_sum = 0
        count = 0
        vowels = 'aeiou'

        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count
        
        for j in range(k, len(s)):
            if s[j] in vowels:
                count += 1

            if s[j-k] in vowels:
                count -= 1
            max_count = max(count, max_count)
        
        return max_count