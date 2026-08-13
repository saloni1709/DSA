class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            seen.add(nums[i])