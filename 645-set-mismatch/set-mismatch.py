class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        seen = set()
        for i in nums:
            if i in seen:
                duplicate = i
            seen.add(i)
        for x in range(1, len(nums)+1):
            if x not in nums:
                missing = x
        return [duplicate, missing]