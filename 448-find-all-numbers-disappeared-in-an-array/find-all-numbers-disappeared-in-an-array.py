class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans = []
        seen = set(nums)
        for i in range(1, len(nums)+1):
            if i not in seen:
                ans.append(i)
        return ans