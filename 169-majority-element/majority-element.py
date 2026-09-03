class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: ints
        """
        
        f = {}
        for i in nums:
            f[i] = f.get(i, 0) + 1

            if f[i] > len(nums)//2:
                return i
        