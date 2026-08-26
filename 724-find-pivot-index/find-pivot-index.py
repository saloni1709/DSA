class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total = sum(nums)
        l = 0
        for i in range(len(nums)):
            pivot = nums[i]
            # total = l + r + pivot
            r = total - l - pivot

            if l == r:
                return i
            l += pivot
            
        return -1