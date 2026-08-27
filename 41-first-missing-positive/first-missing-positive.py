class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        seen = set(nums)
        for i in range(1, len(nums)+1):
            if i not in seen:
                return i
        return len(nums)+1