class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total = sum(nums)
        l = 0

        for i in range(len(nums)):
            r = total - nums[i] - l

            if l == r:
                return i

            l = l + nums[i]

        return -1
        
       