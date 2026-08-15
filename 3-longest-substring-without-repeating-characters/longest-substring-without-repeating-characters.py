class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        st = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in st:
                st.remove(s[l])
                l += 1

            st.add(s[r])
            max_len = max(max_len, r-l+1)
        return max_len
        
        
        