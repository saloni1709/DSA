class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        ans = ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for word in strs:
                if len(word) <= i or ch != word[i]:
                    return ans
            ans += ch
        return ans