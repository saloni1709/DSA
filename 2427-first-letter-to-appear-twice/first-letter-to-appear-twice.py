class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        st = set()
        for ch in s:
            if ch in st:
                return ch
            st.add(ch)